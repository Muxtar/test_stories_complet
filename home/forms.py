from django import forms
from home.models import Contact
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, min_length=3, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your name'
    }))
    email = forms.EmailField(max_length=30, min_length=3, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
    subject = forms.ChoiceField(choices=[(1, 'Teklif'), (2, 'Irad'), (2, 'Sikayet')],widget=forms.Select(attrs={
        'class':'form-control',
        'placeholder':''
    }))
    message = forms.CharField(max_length=30, min_length=3, widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Message'
    }))

class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={
               'class':'form-control',
                'placeholder':_('Your name')
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':_('Email')
            }),
            'subject':forms.Select(attrs={
                'class':'form-control',
                'placeholder':_('subject')
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':_('Message')
            })
            
        }
