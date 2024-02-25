from django import forms
from .models import SpModel, SuzukiokadaModel, Studentaward, YearModel, ArticleModel, KINDS
from ckeditor.widgets import CKEditorWidget


#特別賞
class SpForm(forms.ModelForm):
    
    class Meta:
        model = SpModel
        fields = '__all__'

#学生賞
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Studentaward
        fields = '__all__'

#HODIC賞
class PrizeForm(forms.ModelForm):
    
    class Meta:
        model = YearModel
        fields = '__all__'

#鈴木・岡田記念賞の記事
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = ArticleModel
        fields = '__all__'

#鈴木・岡田記念賞の受賞者
class PrizewinnerForm(forms.ModelForm):
    
    class Meta:
        model = SuzukiokadaModel
        fields = '__all__'

class PrizeSearchForm(forms.Form):
    year = forms.ChoiceField(label='', required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    name_or_affiliation = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '氏名または所属を入力してください。'}))

    def __init__(self, *args, **kwargs):
        super(PrizeSearchForm, self).__init__(*args, **kwargs)

        # SuzukiokadaModel で使用されている YearModel の AD フィールドのデータを取得
        used_years = SuzukiokadaModel.objects.values_list('prizekey__AD', flat=True).distinct()

        # 年のドロップダウンメニューの選択肢を制限
        year_choices = [('', '年度を選択してください。')] + [(str(year), str(year)) for year in used_years]
        self.fields['year'].choices = year_choices

        # 賞名のボタンを作成
        for kind in KINDS:
            self.fields[kind[0]] = forms.BooleanField(label=kind[1], required=False)

