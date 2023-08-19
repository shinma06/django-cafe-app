import re
from django import forms
from .models import News, Menu, Booking
from datetime import datetime

class NewsForm(forms.ModelForm):
    category = forms.ChoiceField(label='カテゴリー', choices=News.CATEGORYS, required=True)

    class Meta:
        model = News
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        img = cleaned_data.get('img')
        alt = cleaned_data.get('alt')

        if img and not alt:
            raise forms.ValidationError('画像が指定されている場合は画像タイトルも入力してください。')
        if not img and alt:
            raise forms.ValidationError('画像が指定されていない場合は画像タイトルを指定することはできません。')

        return cleaned_data

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingForm(forms.ModelForm):
    HOURS_CHOICES = [
        (f"{h:02}:{m:02}", f"{h:02}:{m:02}")
        for h in range(9, 22)
        for m in [0, 30]
        if not ((h == 21 and m == 30) or (h == 9 and m == 0))
        ]

    date = forms.CharField(label="日付", widget=forms.TextInput(attrs={'id': 'datepicker', 'readonly': 'readonly'}))
    time = forms.ChoiceField(label="時間", choices=[('', '-----')] + HOURS_CHOICES, required=True)
    number_of_people = forms.IntegerField(label="人数", initial=1, widget=forms.NumberInput(attrs={'min': '1', 'max': '10'}))

    def clean_date_str(self):
        date = self.cleaned_data['date_str']
        try:
            datetime.strptime(date, '%Y/%m/%d')
        except ValueError:
            raise forms.ValidationError('日付の形式が正しくありません。yyyy/mm/ddの形式で入力してください。')
        
        return date

    class Meta:
        model = Booking
        fields = '__all__'

class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100) 
    message = forms.CharField(label='本文', widget=forms.Textarea)
    full_name = forms.CharField(label='フルネーム', max_length=100)
    email = forms.EmailField(label='Emailアドレス', max_length=100)