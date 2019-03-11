from django import forms
from .models import RecipeModel,UserModel

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = '__all__'


class Userform(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['user_key']