from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('name','phone','profession', 'document' )
		widgets = {
		'name':forms.TextInput(attrs={'placeholder': 'Name'}),
		'phone':forms.TextInput(attrs={'placeholder': 'Phone'}), 
		'profession':forms.TextInput(attrs={'placeholder': 'Profession'}),
		#'document':forms.TextInput(attrs={'type':'file','class':'file-input',}),
		}