from django.contrib import admin

# Register your models here.

# 作成したモデルを管理画面に反映するファイル

from .models import News, Menu, Booking

admin.site.register(News)
admin.site.register(Menu)
admin.site.register(Booking)