from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator  # インポート
from markdown import markdown  # 追加
from django_ckeditor_5.fields import CKEditor5Field

CATEGORY = (("更新情報", "更新情報"), ("お知らせ", "お知らせ"), ("その他", "その他"))


class UpdateModel(models.Model):
    date = models.DateField('更新日', help_text='更新日をカレンダーで選択してください．')  
    content = models.CharField('更新内容', max_length=100, help_text='更新内容を入力してください．')
    link = models.CharField('リンク', max_length=500, help_text='更新したページのリンクを入力してください．')
    category = models.CharField('カテゴリー', max_length=100, choices = CATEGORY, help_text='カテゴリーを選択してください．')
    
    class Meta:
        verbose_name_plural="「更新情報 & News」"
    
    def __str__(self):
        return self.content


class Circular(models.Model):
    name = models.CharField(verbose_name='名前', max_length=80, default='1巻1号（1月発行）', help_text='例) 〇巻〇号（〇月発行），HODIC学生シンポジウム など')
    volume = models.IntegerField(verbose_name='巻数', default='1', validators=[MinValueValidator(1)], null=True, blank=True)
    number = models.IntegerField(verbose_name='号数', default='1', validators=[MinValueValidator(1), MaxValueValidator(4)], null=True, blank=True)
    date = models.DateField(verbose_name='発行日')
    pdf = models.FileField(verbose_name='Circular', upload_to='circular/', validators=[FileExtensionValidator(allowed_extensions=['pdf', ])])
    toc = CKEditor5Field(verbose_name='目次(書式は"Paragraph")', null=True, blank=True)
    
    class Meta:
        db_table = 'circular_list'
        verbose_name = 'circular_name'
        verbose_name_plural = 'circular'
   
    def __str__(self):
        return self.name


class HodicCategory(models.Model):
    name = models.CharField(verbose_name='カテゴリ名', max_length=100)
    
    class Meta:
       db_table = 'hodiccategory_list'
       verbose_name = 'hodiccategory_name'
       verbose_name_plural = 'hodiccategory'
       
    def __str__(self):
        return self.name


class HodicArticle(models.Model):
    category = models.ForeignKey('HodicCategory', on_delete=models.PROTECT, verbose_name="カテゴリ", related_name='hodiccategory', related_query_name='fhodiccategory')
    subtitle = models.CharField(verbose_name='サブタイトル', max_length=100, help_text='サブタイトルを入力してください', null=True, blank=True)
    order = models.IntegerField('順番', default='1', help_text='記事の順番を入力してください．', validators=[MinValueValidator(1), MaxValueValidator(20)])
    article = CKEditor5Field('記事', help_text='記事を入力してください．(書式は"Paragraph")', null=True, blank=True)
    
    class Meta:
        db_table = 'hodicarticle_list'
        verbose_name = 'hodicarticle_name'
        verbose_name_plural = 'hodicarticle'
   
    def __str__(self):
        return self.subtitle


class Manual(models.Model):
    name = models.CharField(verbose_name='名前', max_length=100)
    category = models.CharField(verbose_name='カテゴリー', max_length=100, null=True, blank=True)
    pdf = models.FileField(verbose_name='マニュアル', upload_to='manual/', validators=[FileExtensionValidator(allowed_extensions=['pdf', ])])
    

