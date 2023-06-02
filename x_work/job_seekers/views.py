from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CV
from employers.models import Vacancy
from django.http import JsonResponse
from main.models import Occupation
from job_seekers import services, forms
from django.views.generic import ListView





class VacancySearchView(ListView):
    model = Vacancy
    template_name = 'search_vacancy.html'  # Replace with your template file
    context_object_name = 'vacancies'  # Name of the context variable in the template

    def get_queryset(self):
        queryset = super().get_queryset()
        if len(self.request.GET)!=0:
            occupation = self.request.GET.get('occupation')
            city = self.request.GET.get('city')
            schedule = self.request.GET.get('schedule')
            experience = self.request.GET.get('experience')
            upper_exp, lower_exp = experience.split('|')
            education = self.request.GET.get('education')
            salary = self.request.GET.get('salary')
            work_place = self.request.GET.get('work_place')
            print(self.request.GET)
            if occupation != '':
                print(occupation)
                queryset = queryset.filter(occupation__icontains=occupation)
                print(queryset)
            if city!='':
                print(city)
                queryset = queryset.filter(city__icontains=city)
                print(queryset)
            if schedule != 'false':
                print(schedule)
                queryset = queryset.filter(schedule=schedule)
                print(queryset)
            if experience != 'false|false':
                print(lower_exp)
                print(upper_exp)

                queryset = queryset.filter(experience__gte=int(upper_exp), experience__lte=int(lower_exp))
                print(queryset)
            if education!='false':
                print(education)
                queryset = queryset.filter(education=education)
                print(queryset)
            if salary:
                print(salary)
                queryset = queryset.filter(salary=salary)
                print(queryset)
            if work_place!='false':
                print(work_place)
                queryset = queryset.filter(work_place=work_place)
                print(queryset)


            print(queryset)
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Добавление значений критериев поиска в контексте
        filters = ['occupation', 'city', 'experience', 'schedule','education','occupation','work_place']  # Добавьте все поля фильтрации

        for filter_name in filters:
            value = self.request.GET.get(f'{filter_name}')
            context[filter_name] = value
        print(context)
        return context

@login_required
def cv_list(request, user_id):
    if request.method == 'POST':
        services.CVEditor().delete_cv(request)
        return redirect(request.path)
    else:
        list_of_cv=services.CVShow().get_context_user_cv_list(user_id)
        context = {
            'cv_list': list_of_cv 
        }
        print(list_of_cv)
        return render(request, 'cv_list.html', context=context)


@login_required
def create_cv(request, user_id):
    if request.method=='POST':
        print(len(request.POST.getlist('institution')))
        print(request.POST.getlist('institution')[0])

        services.CVEditor().create_cv(request)
        return render(request, 'create_cv.html')
    else:
        form=forms.CVForm()
        return render(request, 'create_cv.html', {'form':form})


@login_required
def edit_cv(request, cv_id):
    if request.method=='POST':
        # print(request.POST)
        services.CVEditor().edit_cv(request,cv_id)
        context= services.CVShow().get_context_user_cv_show(cv_id)
    
        return render(request, 'edit_cv.html', context=context)
    else:
        context= services.CVShow().get_context_user_cv_show(cv_id)
    
        return render(request, 'edit_cv.html', context=context)
    

@login_required
def show_cv(request, cv_id):
    context=services.CVShow().get_context_user_cv_show(cv_id)
    
    return render(request, 'show_cv.html', context=context)
    

def search_vacancy(request):
    form = forms.VacancySearchForm(request.GET)
    vacancies = []
    
    if form.is_valid():
        vacancies = services.VacancySearchService.search_vacancies(form.cleaned_data)
    
    context = {
        'form': form,
        'vacancies': vacancies,
    }
    
    return render(request, 'search_vacancy.html', context)