from django import forms
from models import prospect

class PostForm(forms.ModelForm):

	class Meta:
		model=prospect
		fields = '__all__'
