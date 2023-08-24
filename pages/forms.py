from django import forms
from .models import News, Menu, Booking
from datetime import datetime
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    category = forms.ChoiceField(label='カテゴリー', choices=News.CATEGORYS, required=True)

    class Meta:
        model = News
        fields = ['category', 'text', 'img', 'alt']

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
    HOURS_CHOICES = [
        (f"{h:02}:{m:02}", f"{h:02}:{m:02}")
        for h in range(9, 22)
        for m in [0, 30]
        if not ((h == 21 and m == 30) or (h == 9 and m == 0))
        ]

    date = forms.CharField(label="日付", widget=forms.TextInput(attrs={'id': 'datepicker', 'readonly': 'readonly'}))
    time = forms.ChoiceField(label="時間", choices=[('', '-----')] + HOURS_CHOICES, required=True)
    number_of_people = forms.IntegerField(label="人数", initial=1, widget=forms.NumberInput(attrs={'min': '1', 'max': '10'}))

    def clean_date(self):
        date_str = self.cleaned_data['date']
        
        # yyyy/mm/dd形式の日付を確認
        try:
            date_obj = datetime.strptime(date_str, '%Y/%m/%d').date()
        except ValueError:
            raise ValidationError("日付はyyyy/mm/dd形式で入力してください。")
        
        return date_obj  # 正しい datetime.date オブジェクトとして返す

    # dateフィールドの値を yyyy/mm/dd 形式のstrとして返す
    def _post_clean(self):
        super()._post_clean()
        if 'date' in self.cleaned_data:
            self.cleaned_data['date'] = self.cleaned_data['date'].strftime('%Y/%m/%d')

    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'email', 'phone_number', 'number_of_people']

class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100) 
    message = forms.CharField(label='本文', widget=forms.Textarea)
    full_name = forms.CharField(label='フルネーム', max_length=40)
    email = forms.EmailField(label='Emailアドレス', max_length=40)