from django.db import models
from markdown import markdown  # 追加
from django_ckeditor_5.fields import CKEditor5Field

TYPE = (("鈴木・岡田記念賞", "鈴木・岡田記念賞"), ("鈴木・岡田賞", "鈴木・岡田賞"), ("鈴木正根賞", "鈴木正根賞"), ("特別賞", "特別賞"), ("学生優秀発表賞", "学生優秀発表賞"), ("学生シンポジウム優秀発表賞", "学生シンポジウム優秀発表賞"),("その他", "その他"))
STYLE = (("PDF", "PDF"), ("html", "html"), ("その他", "その他"))
KINDS = (("技術部門賞", "技術部門賞"), ("技術部門奨励賞", "技術部門奨励賞"), ("貢献賞", "貢献賞"), ("特別賞", "特別賞"), ("芸術部門賞", "芸術部門賞"), ("芸術部門奨励賞", "芸術部門奨励賞"),("その他", "その他"))

class SpModel(models.Model):
    #image = models.ImageField('画像', upload_to='media', help_text='画像を選択してください．')
    #name = models.CharField('画像の名前', max_length=100, help_text='画像の名前を入力してください．')
    name = models.CharField(verbose_name='受賞者名', max_length=50)
    affiliation = models.CharField(verbose_name='所属', max_length=100, null=True, blank=True)
    date = models.DateField(verbose_name='受賞日', null=True, blank=True)
    text = CKEditor5Field(verbose_name='記事', help_text='画像を含めて作成してください。(書式は"Paragraph")', null=True, blank=True)  
    
    class Meta:
       db_table = 'spprize_list'
       verbose_name = 'spprize_name'
       verbose_name_plural = 'hodic_spprize'
       
    def __str__(self):
        return self.name
    
#############################################################################################
class YearModel(models.Model):
    prizekey = models.CharField(verbose_name='賞ID', unique=True, max_length=100, help_text='賞のIDを入力してください．例：2021_鈴木・岡田記念賞')
    AD = models.IntegerField('年度(西暦)', help_text='西暦で入力してください．例：2022')
    year = models.CharField('年度(和暦)', max_length=10, help_text='和暦で入力してください．例：令和4')
    prize_type = models.CharField('賞の種類', max_length=100, choices = TYPE, help_text='賞の種類を選択してください．')
    times = models.IntegerField('回数', help_text='回数を入力してください．例：12  ※「鈴木・岡田記念賞」、「鈴木・岡田賞」、「鈴木正根賞」のみ入力', null=True, blank=True)
    chairman = models.CharField('選考委員長', max_length=100, help_text='選考委員長の名前を入力してください．例：山本 健司(徳島大学) ※「鈴木・岡田記念賞」、「鈴木・岡田賞」、「鈴木正根賞」のみ入力', null=True, blank=True)
    
    class Meta:
        verbose_name_plural="賞の年度テーブル"
    
    def __str__(self):
        return self.prizekey

#############################################################################################
class SuzukiokadaModel(models.Model):
    prizekey = models.ForeignKey(YearModel, on_delete = models.PROTECT, verbose_name="賞ID", help_text='賞のIDを選択してください．', related_name='prizesuzukiokada', related_query_name='fprizesuzukiokada')
    kind = models.CharField('賞の名称', max_length=20, choices = KINDS, help_text='賞の名称を選択してください．')
    name = models.CharField('受賞者・受賞グループ', max_length=100, help_text='受賞者や受賞グループの名前を入力してください．例：吉川 宣一')
    affiliation = models.CharField('所属', max_length=100, help_text='受賞者や受賞グループの所属を入力してください．例：埼玉大学', null=True, blank=True)
    
    class Meta:
        verbose_name_plural="鈴木・岡田記念賞の受賞者テーブル"
    
    def __str__(self):
        #return str(self.prizekey)
        return self.name

#############################################################################################
class ArticleModel(models.Model):
    prizekey = models.ForeignKey(YearModel, on_delete = models.PROTECT, verbose_name="賞ID", help_text='賞のIDを選択してください．', related_name='prizearticle', related_query_name='fprizearticle')
    article_style = models.CharField('記事スタイル', max_length=20, choices = STYLE, help_text='記事スタイルを選択してください．')
    pdf = models.FileField('pdf', upload_to='suzukiokada/', help_text='記事スタイルで「PDF」を選択した場合のみ', null=True, blank=True)
    article = CKEditor5Field('記事', help_text='記事を入力してください．(書式は"Paragraph")', null=True, blank=True)
    
    class Meta:
        verbose_name_plural="鈴木・岡田記念賞の記事テーブル"
    
    def __str__(self):
        return str(self.prizekey)

#############################################################################################
class Studentaward(models.Model):
    prizekey = models.ForeignKey(YearModel, on_delete = models.PROTECT, verbose_name="賞ID", help_text='賞のIDを選択してください．', related_name='prizestudentaward', related_query_name='fprizestudentaward')
    title = models.CharField('タイトル', max_length=100, help_text='発表のタイトルを入力してください．')
    name = models.CharField('氏名', max_length=100, help_text='氏名を入力してください．例：山田 太郎')
    
    class Meta:
        verbose_name_plural="学生賞の受賞者テーブル"
    
    def __str__(self):
        return self.name

