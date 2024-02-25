# -*- coding: utf-8 -*-
from django import forms
from .models import Conference, Schedule, WordCategory, HoloWords, Link, Book, WebBookmark
from ckeditor.widgets import CKEditorWidget


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference        
        fields = '__all__'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule        
        fields = '__all__'

class WordCategoryForm(forms.ModelForm):
    class Meta:
        model = WordCategory        
        fields = '__all__'

class HoloWordsForm(forms.ModelForm):
    class Meta:
        model = HoloWords        
        fields = '__all__'

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link        
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book        
        fields = '__all__'

class WebBookmarkForm(forms.ModelForm):
    class Meta:
        model = WebBookmark        
        fields = '__all__'
