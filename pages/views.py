from django.urls import reverse_lazy
from django.views import generic
from .models import News, Menu
from .forms import NewsForm, ContactForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# ホーム

class IndexView(generic.TemplateView):
    template_name = 'pages/index.html'

# ニュース
class NewsView(generic.ListView):
    template_name = 'pages/news.html'
    model = News
    context_object_name = 'object_list'

# ニュース作成
class CreateNewsView(generic.CreateView):
    template_name = 'pages/news_create.html'
    form_class = NewsForm
    success_url = reverse_lazy('pages:news')

# ニュース更新
class UpdateNewsView(generic.UpdateView):
    model = News
    template_name = 'pages/news_update.html'
    success_url = reverse_lazy('pages:news')

# メニュー
class MenuView(generic.ListView):
    template_name = 'pages/menu.html'
    model = Menu 
    context_object_name = 'object_list'

# メニュー作成
class CreateMenuView(generic.CreateView):
    template_name = 'pages/menu_create.html'
    model = Menu
    fields = {'title', 'img', 'alt'}
    success_url = reverse_lazy('pages:menu')


# メニュー更新
class UpdateMenuView(generic.UpdateView):
    model = Menu
    template_name = 'pages/menu_update.html'
    success_url = reverse_lazy('pages:menu')

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

# コンタクト送信完了
class ContactCompleteView(generic.TemplateView):
    template_name = 'pages/contact_complete.html'
