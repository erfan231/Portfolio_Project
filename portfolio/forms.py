from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label="Name",
    error_messages={'required': 'Please enter your name'},
    widget=forms.TextInput(attrs={'placeholder':'Enter Your Name',
    'class':'input-field',
    'id':'name'}
    ))
    

    email = forms.EmailField(max_length=200 , required=True,
    label="Email",error_messages={'required': 'Please enter your email'}, 
    widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email',
                           'class':'input-field',
                           'id':'email'}))


    message = forms.CharField(required=True,
    label="Message" , error_messages={'required': 'Please enter your message'},
    widget=forms.Textarea(attrs={'placeholder':'Enter Your Message',
    'class':'input-field',
    'id':'message'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

