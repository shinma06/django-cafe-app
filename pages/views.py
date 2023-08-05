from django.views import generic
from .models import News, Menu
from .forms import NewsForm, MenuForm, ContactForm
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.conf import settings

def is_superuser(user):
    return user.is_superuser

# ホーム
class IndexView(generic.TemplateView):
    template_name = 'pages/index.html'

# メニュー
class MenuView(generic.ListView):
    template_name = 'pages/menu.html'
    model = Menu 
    context_object_name = 'object_list'

# メニュー追加
@method_decorator(user_passes_test(is_superuser, login_url='pages:menu'), name='dispatch')
class CreateMenuView(generic.CreateView):
    template_name = 'pages/menu_create.html'
    form_class = MenuForm

    def form_valid(self, form):
        menu = form.save()
        self.request.session['menu_id'] = menu.id
        return redirect('pages:menu-posted')

# メニュー追加完了
class PostedMenuView(generic.TemplateView):
    template_name = 'pages/menu_posted.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_id = self.request.session.get('menu_id')
        if menu_id is not None:
            context['menu'] = Menu.objects.get(id=menu_id)
        return context

    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)

# ニュース
class NewsView(generic.ListView):
    template_name = 'pages/news.html'
    model = News
    context_object_name = 'object_list'

# ニュース作成
@method_decorator(user_passes_test(is_superuser, login_url='pages:news'), name='dispatch')
class CreateNewsView(generic.CreateView):
    template_name = 'pages/news_create.html'
    form_class = NewsForm

    def form_valid(self, form):
        news = form.save()
        self.request.session['news_id'] = news.id
        return redirect('pages:news-posted')

# ニュース投稿完了
class PostedNewsView(generic.TemplateView):
    template_name = 'pages/news_posted.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_id = self.request.session.get('news_id')  # Get the ID of the news instance from session
        if news_id is not None:
            context['news'] = News.objects.get(id=news_id)  # Add the news instance to the context
        return context
    
    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)

# コンタクト
class ContactView(generic.View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']

            # メールの送信
            send_mail(
                f'件名: {subject}',
                f'本文: {message}\n\nフルネーム: {full_name}\nEmailアドレス: {email}',
                settings.EMAIL_HOST_USER,  # 送信元のメールアドレス
                ['###'],  # 送信先のメールアドレス（リストで複数指定可能）
                fail_silently=False,
            )

            return redirect('contact-complete')  # 送信成功時に/contact_complete/へリダイレクト
        return render(request, 'pages/contact.html', {'form': form})

# コンタクト送信成功
class ContactCompleteView(generic.TemplateView):
    template_name = 'pages/contact_complete.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)