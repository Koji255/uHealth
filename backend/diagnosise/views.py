import re

from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse
from django.db.models import Min
 
from diagnosise.forms import TextInputForm
from diagnosise.models import Diagnosis
from diagnosise.utils.ai_request import ai_request

from users.models import User


# Create your views here.
def ai_consultation(request):
    '''Returns to user high probable disease by provided symptomes'''
    if request.method == 'POST':
        form = TextInputForm(data=request.POST)

        if form.is_valid():
            symptoms = re.sub('[[{]}|@#$%^&*()]', '', str(form.cleaned_data['symptoms']))

            ai_query = ai_request(symptoms)

            # Lists of values
            disease_category = ai_query['disease_category']
            description = ai_query['description']

            print(disease_category)

            if request.user.is_authenticated:
                # user = User.objects.get(pk=request.user.pk)

                report = Diagnosis.objects.create(user_id=request.user.pk,
                                                symptoms=symptoms,
                                                disease_category=disease_category,
                                                description=description,
                                                )
                report.save()

            
            return render(request, 'diagnosise/results.html', context={
                # Lists with maximum 3 values
                'disease_category': disease_category,
                'description': description,
            })
    
    else:
        form = TextInputForm()
    
    return render(request, 'diagnosise/symptoms.html', context={'form': form})

