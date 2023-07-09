from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(label='Email')
    subject = forms.CharField(label='件名', max_length=100)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
