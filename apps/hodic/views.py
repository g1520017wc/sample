from django.views import View
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView,CreateView,UpdateView,ListView,DeleteView,)
from .models import UpdateModel, Circular, HodicCategory, HodicArticle, Manual
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .forms import UpdateForm, CircularForm, HodiccategoryForm, HodicarticleForm
from datetime import timedelta


class HodicView(View):
    def get(self, request):
        update_list = UpdateModel.objects.order_by("-date","-id")
        hodicarticle_list = HodicArticle.objects.all()
        params = {
            'update_list': update_list,
            'hodicarticle_list': hodicarticle_list,
        }
        
        return render(request, '../templates/hodic/index.html', params)

def HodicArticleView(request):
    hodicarticle_list = HodicArticle.objects.all()
    params = {'hodicarticle_list': hodicarticle_list}
    
    return render(request, '../templates/hodic/index.html', params)
    
def AboutView(request):
    hodicarticle_list = HodicArticle.objects.all()
    params = {'hodicarticle_list': hodicarticle_list}
    return render(request, '../templates/hodic/about.html', params)
    
def NyukaiView(request):
    hodicarticle_list = HodicArticle.objects.all()
    params = {'hodicarticle_list': hodicarticle_list}
    return render(request, '../templates/hodic/nyukai.html', params)
    

def CircularView(request):
    circular_list = Circular.objects.all().values_list('volume').order_by('-volume').distinct()
    hodicarticle_list = HodicArticle.objects.all()
    now = timezone.datetime.now().date()
    params = {'circular_list': circular_list, 'hodicarticle_list': hodicarticle_list, 'now':now}
    params['circular_url'] = reverse('hodic:circular')
    
    return render(request, '../templates/hodic/circular.html', params)

def TOCView(request, volume):
    circular_list = Circular.objects.all().filter(volume=volume).order_by('-date', '-number')
    hodicarticle_list = HodicArticle.objects.all()
    now = timezone.now().date()
    three_years_ago = now - timedelta(days=3*365)  # 3年前の日付を計算
    params = {'circular_list': circular_list, 'hodicarticle_list': hodicarticle_list, 'now': now, 'three_years_ago': three_years_ago}
    return render(request, '../templates/hodic/toc.html', params)


####################################################################################################################################

#List表示関連のView
@login_required
def updatelist_view(request):
    update_list = UpdateModel.objects.filter()
    params = {'update_list': update_list}
    return render(request, '../templates/hodic/updatelist.html', params)

@login_required
def circularlist_view(request):
    circular_list = Circular.objects.filter()
    params = {'circular_list': circular_list}
    return render(request, '../templates/hodic/circularlist.html', params)

@login_required
def hodiccategorylist_view(request):
    hodiccategory_list = HodicCategory.objects.filter()
    params = {'hodiccategory_list': hodiccategory_list}
    return render(request, '../templates/hodic/hodiccategorylist.html', params)

@login_required
def hodicarticlelist_view(request):
    hodicarticle_list = HodicArticle.objects.filter().order_by('category', 'order')
    params = {'hodicarticle_list': hodicarticle_list}
    return render(request, '../templates/hodic/hodicarticlelist.html', params)

####################################################################################################################################

#登録関連のView
class UpdateCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/hodic/update_registration.html'
    form_class = UpdateForm
    success_url = reverse_lazy('hodic:updatelist')

class CircularCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/hodic/circular_registration.html'
    form_class = CircularForm
    success_url = reverse_lazy('hodic:circularlist')

class HodiccategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/hodic/hodiccategory_registration.html'
    form_class = HodiccategoryForm
    success_url = reverse_lazy('hodic:hodiccategorylist')

class HodicarticleCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/hodic/hodicarticle_registration.html'
    form_class = HodicarticleForm
    success_url = reverse_lazy('hodic:hodicarticlelist')

####################################################################################################################################

#更新関連のView
class UpdateEditView(LoginRequiredMixin, UpdateView):
    model = UpdateModel
    form_class = UpdateForm
    template_name = "../templates/hodic/update_registration.html"
    success_url = reverse_lazy('hodic:updatelist')

class CircularEditView(LoginRequiredMixin, UpdateView):
    model = Circular
    form_class = CircularForm
    template_name = "../templates/hodic/circular_registration.html"
    success_url = reverse_lazy('hodic:circularlist')

class HodiccategoryEditView(LoginRequiredMixin, UpdateView):
    model = HodicCategory
    form_class = HodiccategoryForm
    template_name = "../templates/hodic/hodiccategory_registration.html"
    success_url = reverse_lazy('hodic:hodiccategorylist')

class HodicarticleEditView(LoginRequiredMixin, UpdateView):
    model = HodicArticle
    form_class = HodicarticleForm
    template_name = "../templates/hodic/hodicarticle_registration.html"
    success_url = reverse_lazy('hodic:hodicarticlelist')

####################################################################################################################################

#削除関連のView
class UpdateDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/hodic/update_delete.html'
    model = UpdateModel
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('hodic:updatelist')

class CircularDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/hodic/circular_delete.html'
    model = Circular
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('hodic:circularlist')

class HodiccategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/hodic/hodiccategory_delete.html'
    model = HodicCategory
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('hodic:hodiccategorylist')

class HodicarticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/hodic/hodicarticle_delete.html'
    model = HodicArticle
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('hodic:hodicarticlelist')

####################################################################################################################################

#マニュアル関連のView
@login_required
def manuallist_view(request):
    manuallist_list = Manual.objects.filter()
    params = {'manuallist_list': manuallist_list}
    return render(request, '../templates/hodic/manuallist.html', params)

@login_required
def manual_view(request):
    manual_list = Manual.objects.filter()
    params = {'manual_list': manual_list}
    return render(request, '../templates/hodic/manual.html', params)

