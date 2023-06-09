from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CV
from employers.models import Vacancy
from django.http import JsonResponse
from main.models import Occupation
from job_seekers import services, forms
from django.views.generic import ListView





class VacancySearchView(ListView):
    '''View for vacancy searching'''
    model = Vacancy
    template_name = 'search_vacancy.html'  # Replace with your template file
    context_object_name = 'vacancies'  # Name of the context variable in the template
    paginate_by=5
    def get_queryset(self):
        '''Filtering of jobs by search parameters'''
        queryset = super().get_queryset()
        if len(self.request.GET)!=0:
        
            params = {key: value for key, value in self.request.GET.items() if value and value != 'false' and value != 'None'}
            
            
            if 'occupation' in params:
                queryset = queryset.filter(occupation__icontains=params['occupation'])
            if 'city_id' in params:
                queryset = queryset.filter(city_id=params['city_id'])
            if 'schedule' in params:
                queryset = queryset.filter(schedule=params['schedule'])
            if 'experience' in params:
                upper_exp, lower_exp = params['experience'].split('|')
                if upper_exp == 'none':
                    queryset=queryset.filter(experience__isnull=True)
                else:
                    queryset = queryset.filter(experience__gte=int(upper_exp), experience__lte=int(lower_exp))
            if 'education' in params:
                queryset = queryset.filter(education=params['education'])
            if 'salary' in params:
                queryset = queryset.filter(salary__gte=params['salary'])
            if 'work_place' in params:
                queryset = queryset.filter(work_place=params['work_place'])
            return queryset

    def get_context_data(self, **kwargs):
        '''Adding search criteria values in context'''
        context = super().get_context_data(**kwargs)
        filters = ['occupation', 'city', 'experience', 'schedule','education',
                    'occupation','work_place','salary','city_id'] 

        for filter_name in filters:
            value = self.request.GET.get(f'{filter_name}')
            context[filter_name] = value
        paginator = context['paginator']
        last_page_number = paginator.num_pages
        context['pages_list'] = list(range(1, last_page_number+1))
        return context

@login_required
def cv_list(request, user_id):
    '''display a list of user resumes'''
    if request.method == 'POST':
        services.CVEditor().delete_cv(request) #delet cv
        return redirect(request.path)
    else:
        list_of_cv=services.CVShow().get_context_user_cv_list(user_id)
        context = {
            'cv_list': list_of_cv 
        }
        
        return render(request, 'cv_list.html', context=context)


@login_required
def create_cv(request, user_id):
    '''Create summary'''
    if request.method=='POST':
        services.CVEditor().create_cv(request) 
        return render(request, 'create_cv.html')
    else:
        form=forms.CVForm()
        return render(request, 'create_cv.html', {'form':form})


@login_required
def edit_cv(request, cv_id):
    '''edit user's cv'''
    if request.method=='POST':
        services.CVEditor().edit_cv(request,cv_id)
        context= services.CVShow().get_context_user_cv_show(cv_id)
        return render(request, 'edit_cv.html', context=context)
    else:
        context= services.CVShow().get_context_user_cv_show(cv_id)
        return render(request, 'edit_cv.html', context=context)
    

@login_required
def show_cv(request, cv_id):
    '''show cv information'''
    context=services.CVShow().get_context_user_cv_show(cv_id)
    return render(request, 'show_cv.html', context=context)
    

def search_vacancy(request):
    '''serch cv view'''
    form = forms.VacancySearchForm(request.GET)
    vacancies = []
    if form.is_valid():
        vacancies = services.VacancySearchService.search_vacancies(form.cleaned_data)
    context = {
        'form': form,
        'vacancies': vacancies,
    }
    return render(request, 'search_vacancy.html', context)

def reply_to_vacancy(request, vacancy_id):
    '''apply for the job'''
    if request.user.user_type == 'employer':
        previous_page = request.META.get('HTTP_REFERER')
        return redirect(previous_page)
    else:
        services.reply_to_vacancy(request, vacancy_id)
        previous_page = request.META.get('HTTP_REFERER')
        return redirect(previous_page)