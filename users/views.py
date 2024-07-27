from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from users.forms import LoginForm, UserRegisterForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return render(request, 'index.html')
            else:
                form.add_error(None, 'Invalid username or password')
                return render(request, 'users/login.html', context={'form': form})


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', context={'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'index.html')
        else:
            return redirect('register')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')