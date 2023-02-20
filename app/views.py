from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Exist')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already Exist')
                return redirect('register')
            else: 
                user = User.objects.create(username=username, password = password1, first_name = first_name, last_name = last_name, email = email)
                if user is not None:
                    user.save()
                    return redirect('login')
        else: 
            messages.info(request,'Password does not match')
            return redirect('register')
    else:
          return render(request,'index.html',{})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html',{})
    
def home(request):
    return render(request,'home.html', {})


def logout(request):
    return redirect('login')
    
    