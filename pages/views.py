from django.urls import reverse_lazy
from django.views import generic
from .models import News ,Menu
from .forms import NewsForm

# ホーム

class IndexView(generic.TemplateView):
    template_name = 'pages/index.html'

# ニュース
class NewsView(generic.ListView):
    template_name = 'pages/news.html'
    model = News

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

# # コンタクト
# def contact_form(request):

#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             sender = form.cleaned_data['sender']
#             recipients = [settings.EMAIL_HOST_USER]

#             try:
#                 send_mail(subject, message, sender, recipients)
#             except BadHeaderError:
#                 return HttpResponse('無効なヘッダーが見つかりました。')
#             return redirect('contact_complete')

#     else:
#         form = ContactForm()

#     return render(request, 'pages/contact_form.html', {'form': form})

# # コンタクト送信完了

# class ContactComplateView(generic.TemplateView):
#     template_name = 'pages/contact_complete.html'
