from django.db import models
from django.utils import timezone

# Create your models here.

CATEGORY = (('お店の紹介', 'お店の紹介'), ('期間限定メニュー', '期間限定メニュー'), ('イベント', 'イベント'), ('お客様との会話', 'お客様との会話'))
# CATEGORY = (('promotion', 'お店の紹介'), ('irregularmenu', '期間限定メニュー'), ('event', 'イベント'), ('talk', 'お客様との会話'))

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル',)
    text = models.TextField(verbose_name='本文',)
    created_date = models.DateField(default=timezone.now,)
    img = models.ImageField(null=True, blank=True, verbose_name='画像',)
    alt = models.CharField(max_length=100, verbose_name='画像タイトル',)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY,
        verbose_name='カテゴリー',
    )
    
    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='メニュー名',)
    img = models.ImageField(null=True, blank=True, verbose_name='メニュー画像',)
    alt = models.CharField(max_length=100, verbose_name='画像タイトル',)
    
    def __str__(self):
        return self.title
