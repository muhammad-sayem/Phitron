from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm  # Username, password thake ekhane (AuthenticationForm)
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully!!')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form': form})
    
    else:
        return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)

            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']

                user = authenticate(username = name, password = userpass)   # Check kora hocche user database e ache kina

                if user is not None:
                    messages.success(request, 'Logged in successfully!!')
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully!!')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData(instance = request.user)
        return render(request, './profile.html', {'form': form})
    
    else:
        return redirect('signup')
    
    # if request.user.is_authenticated:
    #     return render(request, 'profile.html', {'user': request.user})
    # else:
    #     return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data=request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)    # Password update korbe
                return redirect('profile')
        else:
            form = PasswordChangeForm(user =request.user)

        return render(request, 'passchange.html', {'form': form})

    else:
        return redirect('login')


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data=request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)    # Password update korbe
                return redirect('profile')
        else:
            form = SetPasswordForm(user =request.user)

        return render(request, 'passchange.html', {'form': form})
    
    else:
        return redirect('login')
    

def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully!!')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData()
        return render(request, './profile.html', {'form': form})
    
    else:
        return redirect('signup')
