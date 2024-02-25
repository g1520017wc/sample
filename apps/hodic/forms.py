from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import UpdateModel, Circular, HodicCategory, HodicArticle
 
 
class AddTaskForm(forms.ModelForm):
    """タスク追加フォーム"""
    class Meta:
        model = UpdateModel
        fields = '__all__'
        widgets = {
            'set_date': AdminDateWidget(),
        }

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = UpdateModel
        fields = '__all__'

class CircularForm(forms.ModelForm):
    
    class Meta:
        model = Circular
        fields = '__all__'

class HodiccategoryForm(forms.ModelForm):
    
    class Meta:
        model = HodicCategory
        fields = '__all__'

class HodicarticleForm(forms.ModelForm):
    
    class Meta:
        model = HodicArticle
        fields = '__all__'
