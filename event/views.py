from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import Event_Form
from django.views.decorators.csrf import csrf_exempt
from .models import Event_Table
# Create your views here.

@csrf_exempt
def event_form(request):
    template = loader.get_template('event_form.html')
    return HttpResponse(template.render())

@csrf_exempt
def event_form_submit(request):
    if request.method == 'POST':
        form = Event_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("submit_form")
        else:
            #form = Event_Form()
            return HttpResponse("data not filled correctly!")
        
     
def submited_form(request):
     template = loader.get_template('success.html')
     return HttpResponse(template.render())

def event_details(request):
    mydetails= Event_Table.objects.all().values()
    template = loader.get_template('submit.html')
    context = {
        'mydata':mydetails,
    }  
    return HttpResponse(template.render(context, request))  
    