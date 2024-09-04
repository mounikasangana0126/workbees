from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'index.html', {'messege':"hello"})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
        
    #     # Authenticate the user
    #     user = authenticate(request, username=username, password=password)
        
    #     if user is not None:
    #         # If credentials are correct, log the user in
    #         login(request, user)
    #         return redirect('home')  # Redirect to a homepage or another view
    #     else:
    #         # If authentication fails, show an error message
    #         messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html',{'messege':'Hello'})