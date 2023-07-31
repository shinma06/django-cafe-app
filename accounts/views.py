from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic
from .forms import SignupForm, LoginForm, RenameForm
from django.http import Http404

# 新規登録
class SignupView(generic.View):
    template_name = 'accounts/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('pages:index')

        form = SignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('accounts:signup_complete')
        return render(request, self.template_name, {'form': form})
    
# 新規登録成功
class SignupCompleteView(generic.TemplateView):
    template_name = 'accounts/signup_complete.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)

# ログイン
class LoginView(generic.View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('pages:index')

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

# ログイン成功
class LoginCompleteView(generic.TemplateView):
    template_name = 'accounts/login_complete.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)

# ログアウト成功
class LogoutCompleteView(generic.TemplateView):
    template_name = 'accounts/logout_complete.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)

# アカウントページ
class AccountEditView(generic.View):
    template_name = 'accounts/account_edit.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        form = RenameForm(initial={'username': request.user.username})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RenameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['username']
            request.user.username = new_username
            request.user.save()
            return redirect('accounts:rename_complete')

        return render(request, self.template_name, {'form': form})

# ユーザーID変更成功
class RenameCompleteView(generic.TemplateView):
    template_name = 'accounts/rename_complete.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)