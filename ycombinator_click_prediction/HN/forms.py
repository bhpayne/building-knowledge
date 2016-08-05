from django import forms

from django.forms import ModelForm

from .models import feedback
from .models import test
from .models import moreless
class feedbackForm(ModelForm):
	class Meta:
		model = feedback
		fields = '__all__'


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class testForm(forms.ModelForm):
	class Meta:
		model = test
		fields = '__all__'



class morelessForm(forms.ModelForm):
	class Meta:
		model = moreless
		fields = '__all__'