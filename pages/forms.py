from django import forms
from .models import News, Menu, Booking
from datetime import datetime

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['category', 'title', 'text', 'img', 'alt']

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
        fields = ['title', 'img', 'alt', 'price']

class BookingForm(forms.ModelForm):
    date = forms.DateField(label="日付", input_formats=['%Y/%m/%d'], widget=forms.TextInput(attrs={'id': 'datepicker', 'readonly': 'readonly'}))
    number_of_people = forms.IntegerField(label="人数", initial=1, widget=forms.NumberInput(attrs={'min': '1', 'max': '10'}))

    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'phone_number', 'number_of_people']

    def clean_date(self):
        return self.cleaned_data['date']

class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100)
    message = forms.CharField(label='本文', widget=forms.Textarea)
    full_name = forms.CharField(label='フルネーム', max_length=100)
    email = forms.EmailField(label='Emailアドレス', max_length=100)