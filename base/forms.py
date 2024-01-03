from django import forms
from django.forms import ModelForm
from .models import Room

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










#ask for category while creating a post and let users search by category(jobs,event,gig etc)