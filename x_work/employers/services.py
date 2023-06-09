from employers.models import Employer, Vacancy
from employers.forms import VacancyForm
from job_seekers.models import CV
from main.models import Cities
from django.db.models import Q




class VacancyEditor:
    '''Vacancy data editor'''
    @staticmethod
    def delete_vacancy(vacancy_id):
        '''delete vacancy'''
        Vacancy.objects.get(id=vacancy_id).delete()
        return True

    @staticmethod
    def update_vacancy(data, model_instance):
        '''update vacancy data'''
        form=VacancyForm(data=data, instance=model_instance)
        if form.is_valid():
            form.save()
            if data['city_id'] and data['city_id']!='None':
                model_instance.city=Cities.objects.get(id=data['city_id'])
                model_instance.save()
            return True
        else:
            errors = form.errors.as_data()
            for field, error_list in errors.items():
                print(f"Поле {field}:")
                for error in error_list:
                    print(f"- {error}")
            return False

    @staticmethod
    def create_vacancy(request, user_id):
        '''create new vacancy'''
        employer=Employer.objects.get(user_id=user_id)
        vacancy=Vacancy.objects.create(employer=employer)
        VacancyEditor().update_vacancy(request.POST, vacancy)
        return True

    @staticmethod
    def edit_vacancy(request,vacancy_id):
        '''edit vacancy'''
        vacancy=Vacancy.objects.get(id=vacancy_id)
        VacancyEditor().update_vacancy(request.POST, model_instance=vacancy)
        return True


class VacancyShow:
    '''display vacancy data'''
    @staticmethod
    def get_context_vacancy_list(user_id):
        '''get list of vacancies for context in templates'''
        employer=Employer.objects.get(user_id=user_id)
        list_of_vacancies=Vacancy.objects.filter(employer=employer)
        return list_of_vacancies


    @staticmethod
    def get_context_vacancy(vacancy_id):
        '''get vacancy data for context in templates'''
        vacancy=Vacancy.objects.get(id=vacancy_id)
        user_id=vacancy.employer.user.id
        context={
            'vacancy':vacancy,
            'user_id':user_id
        }
        return context


def reply_to_cv(request, cv_id):
    '''send feedback to summary'''
    cv = CV.objects.get(id = cv_id)
    employer = Employer.objects.get(user=request.user)
    if employer in cv.feedback.all():
        pass
    else:
        cv.feedback.set([employer])



# class VacancySearchService:
#     @staticmethod
#     def search_vacancies(form_data):
#         query = Vacancy.objects.all()
        
#         search_fields = {
#             'occupation': 'occupation__icontains',
#             'city': 'city__icontains',
#             'schedule': 'schedule',
#             'experience': 'experience__gte',
#             'education': 'education',
#             'salary': 'salary__gte',
#             'work_place': 'work_place',
#             'job_description': 'job_description__icontains',
#             # 'key_skills': 'key_skills__icontains',
#         }
        
#         conditions = Q()
        
#         for field, lookup in search_fields.items():
#             value = form_data.get(field)
#             if value:
#                 conditions |= Q(**{lookup: value})
        
#         query = query.filter(conditions)
        
#         return query

