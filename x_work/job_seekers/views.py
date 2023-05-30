from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CV
from django.http import JsonResponse
from main.models import Occupation
from . import services, forms


@login_required
def cv_list(request, user_id):
    list_of_cv=services.get_cv_list(user_id)
    is_owner = (request.user.id == user_id)
    # cv = get_object_or_404(CV, user_id=user_id)

    context = {
        'cv_list': list_of_cv ,
        'is_owner': is_owner,
    }
    return render(request, 'cv_list.html', context)


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


