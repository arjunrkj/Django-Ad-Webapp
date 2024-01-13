from django import forms
from django.forms import ModelForm
from .models import Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



CATEGORY_CHOICES = [

    ('Gigs', 'Gigs'),
    ('Rentals', 'Rentals'),
    ('Events', 'Events'),
    ('Jobs', 'Jobs'),
    ('News', 'News'),
    ('Meetings', 'Meetings'),
    ('Services', 'Services'),
    ('For sale', 'For sale'),
    ('Activity Partner','Activity Partner'),
]

class RoomForm(ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'placeholder': 'events, jobs, gigs etc'}))

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['location'].widget.attrs['placeholder'] = '(optional)'
        self.fields['contact'].widget.attrs['placeholder'] = '(email, phone number, social handles etc..)'
        self.fields['location'].required = False

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if city:
            # Capitalize the first letter and leave the rest as is
            return city.capitalize()
        return city
    

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["username"].widget = forms.TextInput(attrs={"class": "form-control"})

        self.fields["password1"].label = "Password"
        self.fields["password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})

        self.fields["password2"].label = "Confirm Your Password"
        self.fields["password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})

    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists. Please choose a different one.")

        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1', '')

        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if not any(char.isdigit() for char in password1):
            raise ValidationError("Password must contain at least one digit.")

        if not any(char.isupper() for char in password1):
            raise ValidationError("Password must contain at least one capital letter.")

        return password1

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]









#ask for category while creating a post and let users search by category(jobs,event,gig etc)