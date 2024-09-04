from django.shortcuts import render
from adminmodule.models.authentication import AuthenticationModel

def home(request):
    return render(request,'index.html',{'message':'satish here'})

def authentication (request,email,password):
    queryset=AuthenticationModel.objects.get(email=email)
    if queryset.password==password:
        return render(request,'login.html',{'message':'successfully logined'})
    return render(request,'login.html',{'message':"you entred wrong email or password"})

      

# Create your views here.

