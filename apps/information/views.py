from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView,CreateView,UpdateView,ListView,DeleteView,)
from .models import (Conference, Schedule, WordCategory, HoloWords, Link, Book, WebBookmark, )
from apps.hodic.models import HodicCategory, HodicArticle
from django.db.models import Q, Count, Max, Min
from django.core.paginator import Paginator
from django.utils import timezone
#from .consts import ITEM_PER_PAGE
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ConferenceForm, ScheduleForm, WordCategoryForm, HoloWordsForm, LinkForm, BookForm, WebBookmarkForm
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

def schedule_view(request):
    today = timezone.now().date()
    schedule_list = Schedule.objects.all().filter(closedate__gte=today)
    conference_list = Conference.objects.all().filter(display=True).order_by('period')
    hodicarticle_list = HodicArticle.objects.all()
    params = {'schedule_list': schedule_list, 'conference_list': conference_list, 'hodicarticle_list': hodicarticle_list}
    
    return render(request, '../templates/information/schedule.html', params)

####################################################################

#@login_required(login_url='/accounts/login/') 
#def conferecelist_view(request):
    #conference_list = Conference.objects.all().order_by('period')    
    #params = {'conference_list': conference_list}
    #return render(request, '../templates/information/conf_list.html', params)

def link_view(request):
    society_list = Link.objects.filter( Q(category__iexact="society") ).order_by('order')
    museum_list = Link.objects.filter( Q(category__iexact="museum") ).order_by('order')
    university_list = Link.objects.filter( Q(category__iexact="university") ).order_by('order')
    company_list = Link.objects.filter( Q(category__iexact="company") ).order_by('order')
    individualh_list = Link.objects.filter( Q(category__iexact="individual") ).order_by('order')
    hodicarticle_list = HodicArticle.objects.all()
    params = { 'society_list': society_list, 'museum_list': museum_list, 'university_list' : university_list, 'company_list' : company_list, 'individualh_list' : individualh_list, 'hodicarticle_list': hodicarticle_list}
    
    return render(request, '../templates/information/link.html', params)

####################################################################

def word_view(request):
    word_list = HoloWords.objects.all().order_by('wordname')
    hodicarticle_list = HodicArticle.objects.all()
    params = {'word_list': word_list, 'hodicarticle_list': hodicarticle_list}
    
    return render(request, '../templates/information/word.html', params)

####################################################################

def explanation_view(request, wordname):
    try:
        explanation = get_object_or_404(HoloWords, wordname=wordname)
        explanation_list = HoloWords.objects.filter(wordname=wordname)
        params = {'explanation_list': explanation_list, 'wordname': wordname}
        return render(request, '../templates/information/explanation.html', params)
    except HoloWords.DoesNotExist:
        # データが見つからない場合に404エラーを返す
        raise Http404("HoloWords does not exist")

####################################################################

def book_view(request):
    book_list = Book.objects.all().order_by('name')
    hodicarticle_list = HodicArticle.objects.all()
    params = {'book_list': book_list, 'hodicarticle_list': hodicarticle_list}
    
    return render(request, '../templates/information/book.html', params)

####################################################################


#List表示関連のView

#Conference
@login_required
def conferecelist_view(request):    
    conference_list = Conference.objects.filter()
    params = {'conference_list': conference_list}
    return render(request, '../templates/information/conf_list.html', params)

#Schedule
@login_required
def schedulelist_view(request):    
    schedule_list = Schedule.objects.filter()
    params = {'schedule_list': schedule_list}
    return render(request, '../templates/information/schedule_list.html', params)

#WordCategory
@login_required
def wordcategorylist_view(request):    
    wordcategory_list = WordCategory.objects.filter()
    params = {'wordcategory_list': wordcategory_list}
    return render(request, '../templates/information/wordcategory_list.html', params)

#HoloWords
@login_required
def holowordslist_view(request):    
    holowords_list = HoloWords.objects.filter().order_by('category', 'wordname')
    params = {'holowords_list': holowords_list}
    return render(request, '../templates/information/holowords_list.html', params)

#Link
@login_required
def linklist_view(request):    
    link_list = Link.objects.filter()
    params = {'link_list': link_list}
    return render(request, '../templates/information/link_list.html', params)

#Book
@login_required
def booklist_view(request):    
    book_list = Book.objects.filter()
    params = {'book_list': book_list}
    return render(request, '../templates/information/book_list.html', params)

#WebBookmark
@login_required
def webbookmarklist_view(request):    
    webbookmark_list = WebBookmark.objects.filter()
    params = {'webbookmark_list': webbookmark_list}
    return render(request, '../templates/information/webbookmark_list.html', params)

####################################################################

#登録関連のView

#Conference
class ConferenceCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/information/conf_registration.html'
    form_class = ConferenceForm
    success_url = reverse_lazy('information:conflist')

#Schedule
class ScheduleCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/information/schedule_registration.html'
    form_class = ScheduleForm
    success_url = reverse_lazy('information:schedulelist')

#WordCategory
class WordcategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/information/wordcategory_registration.html'
    form_class = WordCategoryForm
    success_url = reverse_lazy('information:wordcategorylist')

#HoloWords
class HolowordsCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/information/holowords_registration.html'
    form_class = HoloWordsForm
    success_url = reverse_lazy('information:holowordslist')

#Link
class LinkCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/information/link_registration.html'
    form_class = LinkForm
    success_url = reverse_lazy('information:linklist')

#Book
class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/information/book_registration.html'
    form_class = BookForm
    success_url = reverse_lazy('information:booklist')

#WebBookmark
class WebbookmarkCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/information/webbookmark_registration.html'
    form_class = WebBookmarkForm
    success_url = reverse_lazy('information:webbookmarklist')

####################################################################    

#更新関連のView

#Conference
class ConferenceEditView(LoginRequiredMixin, UpdateView):    
    model = Conference
    form_class = ConferenceForm
    template_name = "../templates/information/conf_registration.html"
    success_url = reverse_lazy('information:conflist')

#Schedule
class ScheduleEditView(LoginRequiredMixin, UpdateView):    
    model = Schedule
    form_class = ScheduleForm
    template_name = "../templates/information/schedule_registration.html"
    success_url = reverse_lazy('information:schedulelist')

#WordCategory
class WordcategoryEditView(LoginRequiredMixin, UpdateView):    
    model = WordCategory
    form_class = WordCategoryForm
    template_name = "../templates/information/wordcategory_registration.html"
    success_url = reverse_lazy('information:wordcategorylist')

#HoloWords
class HolowordsEditView(LoginRequiredMixin, UpdateView):    
    model = HoloWords
    form_class = HoloWordsForm
    template_name = "../templates/information/holowords_registration.html"
    success_url = reverse_lazy('information:holowordslist')

#Link
class LinkEditView(LoginRequiredMixin, UpdateView):    
    model = Link
    form_class = LinkForm
    template_name = "../templates/information/link_registration.html"
    success_url = reverse_lazy('information:linklist')

#Book
class BookEditView(LoginRequiredMixin, UpdateView):    
    model = Book
    form_class = BookForm
    template_name = "../templates/information/book_registration.html"
    success_url = reverse_lazy('information:booklist')

#WebBookmark
class WebbookmarkEditView(LoginRequiredMixin, UpdateView):    
    model = WebBookmark
    form_class = WebBookmarkForm
    template_name = "../templates/information/webbookmark_registration.html"
    success_url = reverse_lazy('information:webbookmarklist')

####################################################################

#削除関連のView

#Conference
class ConferenceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/information/conf_delete.html'
    model = Conference    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('information:conflist')

#Schedule
class ScheduleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/information/schedule_delete.html'
    model = Schedule    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('information:schedulelist')

#WordCategory
class WordcategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/information/wordcategory_delete.html'
    model = WordCategory    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('information:wordcategorylist')

#HoloWords
class HolowordsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/information/holowords_delete.html'
    model = HoloWords    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('information:holowordslist')

#Link
class LinkDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/information/link_delete.html'
    model = Link    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('information:linklist')

#Book
class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/information/book_delete.html'
    model = Book    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('information:booklist')

#WebBookmark
class WebbookmarkDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/information/webbookmark_delete.html'
    model = WebBookmark    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('information:webbookmarklist')
