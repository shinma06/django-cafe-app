from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from .models import News ,Menu
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail

# ホーム
def index_view(request):
    return render(request, 'pages/index.html')

# ニュース
class NewsView(ListView):
    template_name = 'pages/news.html'
    model = News

# ニュース作成
class CreateNewsView(CreateView):
    template_name = 'pages/news_create.html'
    model = News
    fields = {'title', 'text', 'img', 'alt', 'category'}
    success_url = reverse_lazy('news')


# ニュース更新
class UpdateNewsView(UpdateView):
    model = News
    template_name = 'pages/news_update.html'
    success_url = reverse_lazy('news')

# メニュー
class MenuView(ListView):
    template_name = 'pages/menu.html'
    model = Menu 

# メニュー作成
class CreateMenuView(CreateView):
    template_name = 'pages/menu_create.html'
    model = Menu
    fields = {'title', 'img', 'alt'}
    success_url = reverse_lazy('menu')


# メニュー更新
class UpdateMenuView(UpdateView):
    model = Menu
    template_name = 'pages/menu_update.html'
    success_url = reverse_lazy('menu')

# コンタクト
def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = [settings.EMAIL_HOST_USER]

            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('contact_complete')

    else:
        form = ContactForm()

    return render(request, 'pages/contact_form.html', {'form': form})

# コンタクト送信完了
def contact_complete(request):
    return render(request, 'pages/contact_complete.html')
