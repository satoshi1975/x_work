from employers.models import Employer, Vacancy
from employers.forms import VacancyForm



class VacancyEditor:

    @staticmethod
    def delete_vacancy(vacancy_id):
        Vacancy.objects.get(id=vacancy_id).delete()
        return True

    @staticmethod
    def update_vacancy(data, model_instance):
        form=VacancyForm(data=data, instance=model_instance)
        if form.is_valid():
            form.save()
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
        employer=Employer.objects.get(user_id=user_id)
        vacancy=Vacancy.objects.create(employer=employer)
        VacancyEditor().update_vacancy(request.POST, vacancy)
        return True

    @staticmethod
    def edit_vacancy(request,vacancy_id):
        vacancy=Vacancy.objects.get(id=vacancy_id)
        VacancyEditor().update_vacancy(request.POST, model_instance=vacancy)
        return True


class VacancyShow:

    @staticmethod
    def get_context_vacancy_list(user_id):
        employer=Employer.objects.get(user_id=user_id)
        list_of_vacancies=Vacancy.objects.filter(employer=employer)
        return list_of_vacancies


    @staticmethod
    def get_context_vacancy(vacancy_id):
        vacancy=Vacancy.objects.get(id=vacancy_id)
        user_id=vacancy.employer.user.id
        context={
            'vacancy':vacancy,
            'user_id':user_id
        }
        return context
