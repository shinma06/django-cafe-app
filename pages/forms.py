from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['category', 'title', 'text', 'img', 'alt']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        category = cleaned_data.get('category')
        img = cleaned_data.get('img')
        alt = cleaned_data.get('alt')

        if img and not alt:
            raise forms.ValidationError('画像が指定されている場合は画像タイトルも入力してください。')

        if not img and alt:
            raise forms.ValidationError('画像が指定されていない場合は画像タイトルを指定することはできません。')

        return cleaned_data
    
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100)
    message = forms.CharField(label='本文', widget=forms.Textarea)
    full_name = forms.CharField(label='フルネーム', max_length=100)
    email = forms.EmailField(label='Emailアドレス', max_length=100)