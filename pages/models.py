from django.db import models
from django.utils import timezone

class News(models.Model):
    CATEGORYS = [
        ('', 'カテゴリーを選択'),
        ('promotion', 'お店の紹介'),
        ('irregularmenu', '期間限定メニュー'),
        ('event', 'イベント'),
        ('talk', 'お客様との会話'),
    ]
    category = models.CharField(null=False, max_length=100, choices=CATEGORYS, verbose_name='カテゴリー',)
    title = models.CharField(null=False, max_length=100, verbose_name='タイトル',)
    text = models.TextField(null=False, verbose_name='本文',)
    img = models.ImageField(null=True, blank=True, verbose_name='画像',)
    alt = models.CharField(null=True, blank=True, max_length=100, verbose_name='画像タイトル',)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(null=False, max_length=50, verbose_name='メニュー名',)
    img = models.ImageField(null=False, verbose_name='メニュー画像',)
    alt = models.CharField(null=False, max_length=50, verbose_name='画像タイトル',)
    price = models.IntegerField(null=False, verbose_name='値段(円)')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    name = models.CharField('名前', max_length=40)
    date = models.DateField('日付')
    time = models.TimeField('時間')
    email = models.EmailField('Emailアドレス', max_length=40, null=True)
    phone_number = models.CharField('電話番号', max_length=15)
    number_of_people = models.PositiveIntegerField('人数', default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'