from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from employers import services, forms
from django.views.generic import ListView
from job_seekers.models import CV
from django.core.paginator import Paginator
from django.urls import reverse


class CVSearchView(ListView):
    '''view for summary search'''
    model = CV
    template_name = 'search_cv.html'  
    context_object_name = 'cv'  
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()

        if len(self.request.GET)!=0:
            params = {key: value for key, value in self.request.GET.items() if value and value != 'false'}
            if 'occupation' in params:
                queryset = queryset.filter(occupation__icontains=params['occupation'])
            if 'city_id' in params:
                queryset = queryset.filter(city_id=params['city_id'])
            if 'schedule' in params:
                queryset = queryset.filter(schedule=params['schedule'])
            if 'experience' in params:
                upper_exp, lower_exp = params['experience'].split('|')
                queryset = queryset.filter(experience__gte=int(upper_exp), experience__lte=int(lower_exp))
            if 'education' in params:
                queryset = queryset.filter(education=params['education'])
            if 'salary' in params:
                queryset = queryset.filter(salary=params['salary'])
            if 'work_place' in params:
                queryset = queryset.filter(work_place=params['work_place'])
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding search criteria values in context
        filters = ['occupation', 'city', 'experience', 'schedule','education','occupation','work_place','city_id','salary']  # Добавьте все поля фильтрации

        for filter_name in filters:
            value = self.request.GET.get(f'{filter_name}')
            context[filter_name] = value
        
        paginator = context['paginator']
        last_page_number = paginator.num_pages
        context['pages_list'] = list(range(1, last_page_number+1))
        return context
        

@login_required
def create_vacancy(request, user_id):
    '''create new vacancy'''
    if request.method == 'POST':
        if services.VacancyEditor().create_vacancy(request, user_id):
            return redirect(reverse('vacancy_list',kwargs={'user_id':user_id}))
        else:
            return redirect(reverse('create_vacancy',kwargs={'user_id':user_id}))
    else:
        form=forms.VacancyForm()
        return render(request, 'create_vacancy.html', {'form':form})

@login_required
def vacancy_list(request,user_id):
    '''display list of vacancies'''
    if request.method=='POST':
        services.VacancyEditor().delete_vacancy(vacancy_id=request.POST['vacancy_id'])
        return redirect(request.path)
    else:
        vacancy_list=services.VacancyShow().get_context_vacancy_list(user_id)#get context from list 
                                                                            #of vacancies for template
        
        context={
            'vacancy_list':vacancy_list
        }
        return render(request, 'vacancy_list.html', context=context)

@login_required
def show_vacancy(request, vacancy_id):
    '''Show data of vacancy'''
    context=services.VacancyShow().get_context_vacancy(vacancy_id) #get context from vaca

    return render(request, 'show_vacancy.html', context=context )


@login_required
def edit_vacancy(request, vacancy_id):
    '''Edit vacancy data'''
    if request.method=='POST':
        services.VacancyEditor().edit_vacancy(request,vacancy_id) #edit vacancy data
        context=services.VacancyShow().get_context_vacancy(vacancy_id) #get vacancy data for template context
        return render(request, 'edit_vacancy.html', context=context)
    else:
        context=services.VacancyShow().get_context_vacancy(vacancy_id)#get vacancy data for template context
        return render(request, 'edit_vacancy.html', context=context)

def reply_to_cv(request, cv_id):
    '''send feedback to summary'''
    previous_page = request.META.get('HTTP_REFERER')
    if request.user.user_type == 'jobseeker' or not request.user.is_authenticated:
        return redirect(previous_page)
    else:
        services.reply_to_cv(request, cv_id)
        return redirect(previous_page)



# def search_vacancy(request):
#     form = forms.VacancySearchForm(request.GET)
#     vacancies = []
    
#     if form.is_valid():
#         vacancies = services.VacancySearchService.search_vacancies(form.cleaned_data)
    
#     context = {
#         'form': form,
#         'vacancies': vacancies,
#     }
    
#     return render(request, 'vacancy_search.html', context)

