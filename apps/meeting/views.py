from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,UpdateView,ListView,DeleteView,)
from .models import Footer, MeetingCategory, Meeting, Presentation
from apps.hodic.models import HodicCategory, HodicArticle
from django.db.models import Max, Min
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .forms import MeetingForm, PresentationForm, FooterForm, MeetingcategoryForm, MeetingSearchForm
from django.http import Http404



def meeting_view(request):
    meeting_list = Meeting.objects.filter().order_by('-date')
    now = timezone.datetime.now()
    hodicarticle_list = HodicArticle.objects.all()

    # フォームの提出を処理
    if request.method == 'GET':
        # Meeting モデルの年の一覧を取得し、フォームにセット
        years = Meeting.objects.dates('date', 'year')
        year_choices = [('', '年度を選択してください。')] + [(year.year, str(year.year)) for year in years]
        form = MeetingSearchForm(request.GET)
        form.fields['year'].choices = year_choices

        if form.is_valid():
            year = form.cleaned_data.get('year')
            if year:
                meeting_list = meeting_list.filter(date__year=year)
    else:
        # GET パラメータがない場合、フォームの初期値を空にする
        form = MeetingSearchForm()

    params = {'meeting_list': meeting_list, 'now': now, 'form': form, 'hodicarticle_list': hodicarticle_list }
    params['meeting_url'] = reverse('meeting:meeting')

    return render(request, '../templates/meeting/meeting.html', params)

#def meeting_view(request):
    #meeting_list = Meeting.objects.all().filter(key='2023_3')
    #latest = Meeting.objects.aggregate(Max('date'))    
    #meeting_1 = Meeting.objects.all().get(date=latest['date__max'])
    #value = 0
    #params = {'meeting_1': meeting_1, 'value':value}
    
    #return render(request, '../templates/meeting/meeting.html', params)

def DetailView(request, detailkey):
    try:
        detail = Meeting.objects.get(key=detailkey)
        detail_list = Presentation.objects.all().filter(key__id=detail.id).order_by('order')
        params = {'detail_list': detail_list, 'detailkey': detailkey}
        return render(request, '../templates/meeting/detail.html', params)
    except Meeting.DoesNotExist:
        # データが見つからない場合に404エラーを返す
        raise Http404("Meeting does not exist")

    
class MeetinglogView(ListView):
    template_name = "../templates/meeting/meetinglog.html"
    model = Footer
    
    def get_context_data(self, **kwargs):
        context = super(MeetinglogView, self).get_context_data(**kwargs)
        context.update({
            'object_Year': Meeting.objects.order_by("-key",),
            'object_Lecture': Presentation.objects.all(),
        })
        return context

############################################################################################

#List表示関連のView
@login_required
def meetinglist_view(request):    
    meeting_list = Meeting.objects.filter()
    params = {'meeting_list': meeting_list}
    return render(request, '../templates/meeting/meetinglist.html', params)

@login_required
def presenlist_view(request, meetingkey):
    meeting = Meeting.objects.get(key=meetingkey)
    presentation_list = Presentation.objects.all().filter(key__id=meeting.id).order_by('order')
    params = {'presentation_list': presentation_list, 'meetingkey': meetingkey}
    return render(request, '../templates/meeting/presentationlist.html', params)

@login_required
def footerlist_view(request):    
    footer_list = Footer.objects.filter()
    params = {'footer_list': footer_list}
    return render(request, '../templates/meeting/footerlist.html', params)

@login_required
def meetingcategorylist_view(request):    
    meetingcategory_list = MeetingCategory.objects.filter()
    params = {'meetingcategory_list': meetingcategory_list}
    return render(request, '../templates/meeting/meetingcategorylist.html', params)

#登録関連のView
class MeetingCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/meeting/meeting_registration.html'
    form_class = MeetingForm
    success_url = reverse_lazy('meeting:meetinglist')

class PresenCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/meeting/presen_registration.html'
    form_class = PresentationForm
    #success_url = reverse_lazy('report:themelist')
    
    def get_initial(self):
        code = self.kwargs['meetingkey']
        meeting = Meeting.objects.get(key=code)
        initial = super().get_initial()
        print(meeting.key)
        initial['key'] = meeting.id        
        return initial
    
    def get_success_url(self):
        return reverse('meeting:presenlist', kwargs={'meetingkey': self.kwargs['meetingkey']})
    
class FooterCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/meeting/footer_registration.html'
    form_class = FooterForm
    success_url = reverse_lazy('meeting:footerlist')

class MeetingcategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = '../templates/meeting/meetingcategory_registration.html'
    form_class = MeetingcategoryForm
    success_url = reverse_lazy('meeting:meetingcategorylist')


#更新関連のView
class MeetingEditView(LoginRequiredMixin, UpdateView):    
    model = Meeting
    form_class = MeetingForm
    template_name = "../templates/meeting/meeting_registration.html"
    success_url = reverse_lazy('meeting:meetinglist')


class PresenEditView(LoginRequiredMixin, UpdateView):    
    model = Presentation
    form_class = PresentationForm
    template_name = "../templates/meeting/presen_registration.html"
    #success_url = reverse_lazy('report:titlelist')
    
    def get_success_url(self):
        return reverse('meeting:presenlist', kwargs={'meetingkey': self.kwargs['meetingkey']})


class FooterEditView(LoginRequiredMixin, UpdateView):    
    model = Footer
    form_class = FooterForm
    template_name = "../templates/meeting/footer_registration.html"
    success_url = reverse_lazy('meeting:footerlist')


class MeetingcategoryEditView(LoginRequiredMixin, UpdateView):    
    model = MeetingCategory
    form_class = MeetingcategoryForm
    template_name = "../templates/meeting/meetingcategory_registration.html"
    success_url = reverse_lazy('meeting:meetingcategorylist')


#削除関連のView
class MeetingDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/meeting/meeting_delete.html'
    model = Meeting    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('meeting:meetinglist')

class PresenDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/meeting/presen_delete.html'
    model = Presentation    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('meeting:presenlist', kwargs={'meetingkey': self.kwargs['meetingkey']})

class FooterDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/meeting/footer_delete.html'
    model = Footer
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('meeting:footerlist')

class MeetingcategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = '../templates/meeting/meetingcategory_delete.html'
    model = MeetingCategory
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        return obj
    
    def get_success_url(self):
        return reverse('meeting:meetingcategorylist')