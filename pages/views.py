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

# メニュー追加(superuserのみ使用可)
@method_decorator(user_passes_test(is_superuser, login_url='pages:menu'), name='dispatch')
class CreateMenuView(generic.CreateView):
    template_name = 'pages/menu_create.html'
    form_class = MenuForm
    success_url = reverse_lazy('pages:menu-posted')

    # 作成されたインスタンスのIDをセッションに保存
    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['menu_id'] = self.object.id
        return response

# メニュー追加完了
class PostedMenuView(generic.TemplateView):
    template_name = 'pages/menu_posted.html'

    # セッションからインスタンスのIDを取得し作成されたインスタンスを特定
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_id = self.request.session.get('menu_id')
        context['posted_menu'] = Menu.objects.get(id=menu_id)
        return context

    #リダイレクト以外の方法でのアクセスを禁止
    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)

# ニュース
class NewsView(generic.ListView):
    template_name = 'pages/news.html'
    model = News
    context_object_name = 'object_list'

# ニュース絞り込み
class NewsCategoryView(generic.ListView):
    template_name = 'pages/news.html'
    model = News
    context_object_name = 'object_list'

    def get_queryset(self):
        category = self.kwargs['category']
        valid_categories = [cat[0] for cat in News.CATEGORY]
        if category not in valid_categories:
            raise Http404("Category does not exist")
        self.category_name = dict(News.CATEGORY).get(category)
        return News.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.category_name
        return context

# ニュース作成(superuserのみ使用可)
@method_decorator(user_passes_test(is_superuser, login_url='pages:news'), name='dispatch')
class CreateNewsView(generic.CreateView):
    template_name = 'pages/news_create.html'
    form_class = NewsForm
    success_url = reverse_lazy('pages:news-posted')

    # 作成されたインスタンスのIDをセッションに保存
    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['news_id'] = self.object.id
        return response

# ニュース投稿完了
class PostedNewsView(generic.TemplateView):
    template_name = 'pages/news_posted.html'

    # セッションからインスタンスのIDを取得し作成されたインスタンスを特定
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_id = self.request.session.get('news_id')
        context['posted_news'] = Menu.objects.get(id=news_id)
        return context
    
    #リダイレクト以外の方法でのアクセスを禁止
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

            return redirect('contact-complete')
        return render(request, 'pages/contact.html', {'form': form})

# コンタクト送信成功
class ContactCompleteView(generic.TemplateView):
    template_name = 'pages/contact_complete.html'

    #リダイレクト以外の方法でのアクセスを禁止
    def dispatch(self, *args, **kwargs):
        if not self.request.META.get('HTTP_REFERER'):
            raise Http404("Page not found")
        return super().dispatch(*args, **kwargs)