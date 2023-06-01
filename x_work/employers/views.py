from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from employers import services, forms


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