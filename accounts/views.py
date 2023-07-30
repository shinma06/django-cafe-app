from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic
from .forms import SignupForm, LoginForm

class SignupView(generic.View):
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('pages:index')
        return render(request, self.template_name, {'form': form})

class LoginView(generic.View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:login_complete')
            else:
                form.add_error(None, 'ユーザー名かパスワードが間違っています.')
        return render(request, 'accounts/login.html', {'form': form})
    
class LoginCompleteView(generic.TemplateView):
    template_name = 'accounts/login_complete.html'

class LogoutCompleteView(generic.TemplateView):
    template_name = 'accounts/logout_complete.html'