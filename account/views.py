from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterUserForm


def LoginView(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Aydemir Hırdavata Giriş Yaptınız. İyi alışverişler Dileriz.'))
            return redirect('index')
        else:
            messages.success(request, ('Kullanıcı Adı veya Parola Hatalı . Lütfen Tekrar Deneyin...'))
            return redirect('login')
    return render(request, 'account/login.html')

def LogoutView(request):
    logout(request)
    return redirect('index')


def RegisterView(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Müşteri kaydı oluşturuldu. Müşteri girişi yapabilirsiniz.'))
            return redirect('login')
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterUserForm()

    return render(request, "account/register.html", {"form": form})


def AdresView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
    

        user = User(first_name=first_name, last_name=last_name, email = email)
        user.save()
        messages.success(request, 'Bilgiler kaydedilmiştir')
        return redirect('index')
   
    else:
        return render(request, 'account/adres.html')

