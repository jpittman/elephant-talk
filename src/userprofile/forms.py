from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import UserProfile


class UserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and password.
    """
    username = forms.RegexField(max_length=30, regex=r'^[\w.@+-]+$',
        help_text = ("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': ("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField()
        
    class Meta:
        model = User
        fields = ("username",)
        
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(("A user with that username already exists."))
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(("A user with that email already exists."))

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserProfileForm(forms.Form):

    first_name = forms.RegexField(max_length=30, regex=r'^[\w-]+$',
        help_text = ("Required. 30 characters or fewer. Letters, digits and '-' only."),
        error_messages = {'invalid': ("This value may contain only letters, numbers and '-' characters.")})

    last_name = forms.RegexField(max_length=30, regex=r'^[\w-]+$',
        help_text = ("Required. 30 characters or fewer. Letters, digits and '-' only."),
        error_messages = {'invalid': ("This value may contain only letters, numbers and '-' characters.")})

    email = forms.EmailField()
    
    bio = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = UserProfile
        fields = ("user.username",)
        