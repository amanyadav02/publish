from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import requests,json
# Create your views here.
def index(request):
    if(request.method=='POST'):
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        r=requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&amp;lastName=' + lastname)
        json_data=json.loads(r.text)
        joke=json_data.get('value').get('joke')
        context={
            'joker':joke,
        }
        return render(request,'mysite/index.html',context)
    else:
        firstname="Aman"
        lastname="Yadav"
        r=requests.get('http://api.icndb.com/jokes/random?firstName='+firstname+'&amp;lastName='+lastname)
        json_data=json.loads(r.text)
        joke=json_data.get('value').get('joke')
        context={
            'joker':joke,
        }
        return render(request,'mysite/index.html',context)
def portfolio(request):
    return render(request,'mysite/portfolio.html')
def contact(request):
    if(request.method=='POST'):
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        c=Contact(email=email,subject=subject,message=message)
        c.save()
        return render(request,'mysite/thank.html')
    else:
        return render(request,'mysite/contact.html')
