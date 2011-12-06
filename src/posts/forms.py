from django import forms
# from django.forms.extras.widgets import SelectDateWidget

class PostForm(forms.Form):
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'size':'50'}))
    body = forms.CharField(widget=forms.Textarea)