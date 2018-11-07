from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'personalwebapp/home.html')

def contact(request):
	return render(request, 'personalwebapp/contact.html',{'content':['Advait Joshi','joshiadvait8@gmail.com']})
	
