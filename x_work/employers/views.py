from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from employers import services, forms
from django.views.generic import ListView
from job_seekers.models import CV
from django.core.paginator import Paginator


class CVSearchView(ListView):
    model = CV
    template_name = 'search_cv.html'  # Replace with your template file
    context_object_name = 'cv'  # Name of the context variable in the template
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
                print(upper_exp, lower_exp)
                queryset = queryset.filter(experience__gte=int(upper_exp), experience__lte=int(lower_exp))
            if 'education' in params:
                queryset = queryset.filter(education=params['education'])
            if 'salary' in params:
                queryset = queryset.filter(salary=params['salary'])
            if 'work_place' in params:
                queryset = queryset.filter(work_place=params['work_place'])


            print(queryset)
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        


        # Добавление значений критериев поиска в контексте
        filters = ['occupation', 'city', 'experience', 'schedule','education','occupation','work_place','city_id']  # Добавьте все поля фильтрации

        for filter_name in filters:
            value = self.request.GET.get(f'{filter_name}')
            context[filter_name] = value
        
        paginator = context['paginator']
        last_page_number = paginator.num_pages
        context['pages_list'] = list(range(1, last_page_number+1))
        return context
        





@login_required
def create_vacancy(request, user_id):
    print(request.POST)
    if request.method == 'POST':
        services.VacancyEditor().create_vacancy(request, user_id)
        return redirect(request.path)
    else:
        form=forms.VacancyForm()
        return render(request, 'create_vacancy.html', {'form':form})

@login_required
def vacancy_list(request,user_id):
    if request.method=='POST':
        services.VacancyEditor().delete_vacancy(vacancy_id=request.POST['vacancy_id'])
        return redirect(request.path)
    else:
        vacancy_list=services.VacancyShow().get_context_vacancy_list(user_id)
        context={
            'vacancy_list':vacancy_list
        }
        print(vacancy_list)
        return render(request, 'vacancy_list.html', context=context)

@login_required
def show_vacancy(request, vacancy_id):
    context=services.VacancyShow().get_context_vacancy(vacancy_id)

    return render(request, 'show_vacancy.html', context=context )


@login_required
def edit_vacancy(request, vacancy_id):
    if request.method=='POST':
        services.VacancyEditor().edit_vacancy(request,vacancy_id)
        context=services.VacancyShow().get_context_vacancy(vacancy_id)
        return render(request, 'edit_vacancy.html', context=context)
    else:
        context=services.VacancyShow().get_context_vacancy(vacancy_id)
        return render(request, 'edit_vacancy.html', context=context)



def search_vacancy(request):
    form = forms.VacancySearchForm(request.GET)
    vacancies = []
    
    if form.is_valid():
        vacancies = services.VacancySearchService.search_vacancies(form.cleaned_data)
    
    context = {
        'form': form,
        'vacancies': vacancies,
    }
    
    return render(request, 'vacancy_search.html', context)