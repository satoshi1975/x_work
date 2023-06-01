from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CV
from django.http import JsonResponse
from main.models import Occupation
from job_seekers import services, forms


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
    

