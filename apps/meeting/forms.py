from django import forms
from .models import Footer, MeetingCategory, Meeting, Presentation
from ckeditor.widgets import CKEditorWidget

class MeetingForm(forms.ModelForm):
    
    class Meta:
        model = Meeting
        fields = '__all__'
            
            
class PresentationForm(forms.ModelForm):
    disabled_fields = ('key',)
    
    class Meta:
        model = Presentation
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PresentationForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True


class FooterForm(forms.ModelForm):
    
    class Meta:
        model = Footer
        fields = '__all__'


class MeetingcategoryForm(forms.ModelForm):
    
    class Meta:
        model = MeetingCategory
        fields = '__all__'


class MeetingSearchForm(forms.Form):
    year = forms.ChoiceField(
        label='',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[('', '年度を選択してください。')] + [(year.year, str(year.year)) for year in Meeting.objects.dates('date', 'year')]
    )