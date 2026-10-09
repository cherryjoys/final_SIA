from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event

        fields = [
            'event_id',
            'event_name',
            'description',
            'date',
            'time',
            'location',
            'number_of_participants',
            'status',
            'organizer',
        ]

        widgets = {
            'event_id': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Event ID'
            }),

            'event_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Event Name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Event Description',
                'rows': 3
            }),

            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }),

            'number_of_participants': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of Participants',
                'min': '0'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'organizer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Organizer'
            }),
        }