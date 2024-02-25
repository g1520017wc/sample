from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,UpdateView,ListView,DeleteView,)
from django.views.generic import ListView
from .models import SpModel, SuzukiokadaModel, Studentaward, YearModel, ArticleModel
from apps.hodic.models import HodicCategory, HodicArticle
from django.db.models import Max, Min, Q
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SpForm, StudentForm, PrizeForm, ArticleForm, PrizewinnerForm, PrizeSearchForm
from django.http import Http404


def PrizeView(request):
    hodicarticle_list = HodicArticle.objects.all()
    params = {'hodicarticle_list': hodicarticle_list}
    
    return render(request, '../templates/prize/prize.html', params)
    

    #def get_context_data(self, **kwargs):
        #context = super(PrizeView, self).get_context_data(**kwargs)
        #context['object_list1'] = SymposiumModel.objects.order_by("-year","title","-id",)
        #context['object_list2'] = Studentaward.objects.order_by("prizekey","title","-id",)
        #return context
    
class SpView(ListView):
    template_name = '../templates/prize/sp.html'
    model = SpModel

class CommemorativeView(ListView):
    template_name = '../templates/prize/commemorative.html'
    model = SuzukiokadaModel
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = SuzukiokadaModel.objects.all().select_related().order_by("-prizekey")
        year_filter = self.request.GET.get('year')
        kind_filter = self.request.GET.get('kind')
        name_or_affiliation_filter = self.request.GET.get('name_or_affiliation')

        if year_filter:
            queryset = queryset.filter(prizekey__AD=year_filter)

        if kind_filter:
            queryset = queryset.filter(kind=kind_filter)

        if name_or_affiliation_filter:
            queryset = queryset.filter(
                Q(name__icontains=name_or_affiliation_filter) | 
                Q(affiliation__icontains=name_or_affiliation_filter)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PrizeSearchForm(self.request.GET)
        context['clear_filter_button'] = True
        return context

def ArticleView(request, articlekey):
    try:
        article = YearModel.objects.get(prizekey=articlekey)
        article_list = ArticleModel.objects.filter(prizekey=article).order_by('prizekey')
        params = {'article_list': article_list, 'articlekey': articlekey}
        return render(request, '../templates/prize/article.html', params)
    except YearModel.DoesNotExist:
        # データが見つからない場合に404エラーを返す
        raise Http404("YearModel does not exist")


def ExcellenceView(request):
    hodicarticle_list = HodicArticle.objects.all()
    studentaward_list = Studentaward.objects.order_by("-prizekey","title","-id",)
    params = {
        'hodicarticle_list': hodicarticle_list,
        'studentaward_list': studentaward_list,
        }
    
    return render(request, '../templates/prize/excellence.html', params)

def SymposiumView(request):
    hodicarticle_list = HodicArticle.objects.all()
    studentaward_list = Studentaward.objects.order_by("-prizekey","title","-id",)
    params = {
        'hodicarticle_list': hodicarticle_list,
        'studentaward_list': studentaward_list,
        }
    
    return render(request, '../templates/prize/symposium.html', params)


############################################################################################

#List表示関連のView

#特別賞
@login_required
def splist_view(request):    
    sp_list = SpModel.objects.filter()
    params = {'sp_list': sp_list}
    return render(request, '../templates/prize/splist.html', params)

#学生賞
@login_required
def studentlist_view(request):    
    student_list = Studentaward.objects.filter()
    params = {'student_list': student_list}
    return render(request, '../templates/prize/studentlist.html', params)

#HODIC賞
@login_required
def prizelist_view(request):    
    prize_list = YearModel.objects.filter()
    params = {'prize_list': prize_list}
    return render(request, '../templates/prize/prizelist.html', params)

#鈴木・岡田記念賞の記事
@login_required
def articlelist_view(request):    
    article_list = ArticleModel.objects.filter()
    params = {'article_list': article_list}
    return render(request, '../templates/prize/articlelist.html', params)

#鈴木・岡田記念賞の受賞者
@login_required
def prizewinnerlist_view(request):    
    prizewinner_list = SuzukiokadaModel.objects.filter()
    params = {'prizewinner_list': prizewinner_list}
    return render(request, '../templates/prize/prizewinnerlist.html', params)


############################################################################################

#登録関連のView

#特別賞
class SpCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/prize/sp_registration.html'
    form_class = SpForm
    success_url = reverse_lazy('prize:splist')

#学生賞
class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/prize/student_registration.html'
    form_class = StudentForm
    success_url = reverse_lazy('prize:studentlist')

#HODIC賞
class PrizeCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/prize/prize_registration.html'
    form_class = PrizeForm
    success_url = reverse_lazy('prize:prizelist')

#鈴木・岡田記念賞の記事
class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/prize/article_registration.html'
    form_class = ArticleForm
    success_url = reverse_lazy('prize:articlelist')

#鈴木・岡田記念賞の受賞者
class PrizewinnerCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/prize/prizewinner_registration.html'
    form_class = PrizewinnerForm
    success_url = reverse_lazy('prize:prizewinnerlist')


############################################################################################

#更新関連のView

#特別賞
class SpEditView(LoginRequiredMixin, UpdateView):    
    model = SpModel
    form_class = SpForm
    template_name = "../templates/prize/sp_registration.html"
    success_url = reverse_lazy('prize:splist')

#学生賞
class StudentEditView(LoginRequiredMixin, UpdateView):    
    model = Studentaward
    form_class = StudentForm
    template_name = "../templates/prize/student_registration.html"
    success_url = reverse_lazy('prize:studentlist')

#HODIC賞
class PrizeEditView(LoginRequiredMixin, UpdateView):    
    model = YearModel
    form_class = PrizeForm
    template_name = "../templates/prize/prize_registration.html"
    success_url = reverse_lazy('prize:prizelist')

#鈴木・岡田記念賞の記事
class ArticleEditView(LoginRequiredMixin, UpdateView):    
    model = ArticleModel
    form_class = ArticleForm
    template_name = "../templates/prize/article_registration.html"
    success_url = reverse_lazy('prize:articlelist')

#鈴木・岡田記念賞の受賞者
class PrizewinnerEditView(LoginRequiredMixin, UpdateView):    
    model = SuzukiokadaModel
    form_class = PrizewinnerForm
    template_name = "../templates/prize/prizewinner_registration.html"
    success_url = reverse_lazy('prize:prizewinnerlist')


############################################################################################

#削除関連のView

#特別賞
class SpDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/prize/sp_delete.html'
    model = SpModel    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('prize:splist')

#学生賞
class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/prize/student_delete.html'
    model = Studentaward    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('prize:studentlist')

#HODIC賞
class PrizeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/prize/prize_delete.html'
    model = YearModel    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('prize:prizelist')

#鈴木・岡田記念賞の記事
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/prize/article_delete.html'
    model = ArticleModel    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('prize:articlelist')

#鈴木・岡田記念賞の受賞者
class PrizewinnerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/prize/prizewinner_delete.html'
    model = SuzukiokadaModel    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('prize:prizewinnerlist')
