import os

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator  # インポート
from markdown import markdown  # 追加
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

CATEGORY_LINK = (('society', '学会・協会・研究会'),('museum', '美術館・科学館・博物館'),('university','大学関連'),('company','企業'),('individual','個人'))

############################################################################
class Conference(models.Model):
    name = models.CharField(verbose_name='学会名（表示用）',max_length=150)
    name_ja = models.CharField(verbose_name='学会和名',max_length=150, blank=True, null=True)
    name_en = models.CharField(verbose_name='学会英名',max_length=150, blank=True, null=True)
    period_disp = models.CharField(verbose_name='開催時期（表示用）',max_length=80, blank=True, null=True)
    period = models.CharField(verbose_name='開催時期（ソート用）',max_length=4, help_text='おおよその時期を入力，例 3月中旬 → 0315', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    display = models.BooleanField(verbose_name='表示・非表示', help_text='表示する場合True', default=False)
    
    class Meta:
       db_table = 'conference_list'
       verbose_name = 'conference_name'
       verbose_name_plural = 'conference'
       
    def __str__(self):
        return self.name
    
############################################################################
class Schedule(models.Model):
    name = models.ForeignKey('Conference', on_delete = models.PROTECT, verbose_name="学会名", default='HODIC', related_name='schedule', related_query_name='fschdule')
    opendate = models.DateField(verbose_name='開始日')
    closedate = models.DateField(verbose_name='終了日', help_text='1日開催の場合は開始日と同じにしてください。')    
    deadline = models.DateField(verbose_name='投稿締切日', blank=True, null=True)
    url = models.URLField(blank=True, null=True)    
    
    class Meta:
       db_table = 'schedule_list'
       verbose_name = 'schedule_name'
       verbose_name_plural = 'schedule'
       
    def Conference(self):
        return self.name

############################################################################    
class WordCategory(models.Model):
    name = models.CharField(verbose_name='カテゴリ名',max_length=100)
    
    class Meta:
       db_table = 'category_list'
       verbose_name = 'category_name'
       verbose_name_plural = 'wordcategory'
       
    def __str__(self):
        return self.name

############################################################################
class HoloWords(models.Model):
    wordname = models.CharField(verbose_name='用語',max_length=80,blank=True, null=True)
    wordename = models.CharField(verbose_name='用語(英)',max_length=120,blank=True, null=True)
    abbreviation = models.CharField(verbose_name='略語',max_length=50,blank=True, null=True)
    category = models.ForeignKey('WordCategory', on_delete=models.PROTECT, verbose_name="カテゴリ", related_name='holoword', related_query_name='fholoword')
    article = CKEditor5Field(verbose_name='解説記事(書式は"Paragraph")',blank=True, null=True)
    display = models.BooleanField(verbose_name='掲載可否', default=False)
    
    class Meta:
       db_table = 'word_list'
       verbose_name = 'word_name'
       verbose_name_plural = 'holowords'
       
    def __str__(self):
        return self.wordname

############################################################################    
class Link(models.Model):
    title = models.CharField(verbose_name='タイトル',max_length=150)
    order = models.IntegerField(verbose_name='ソート順')
    introduction = models.TextField(verbose_name='紹介')
    thumbnail = models.ImageField(upload_to='link/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    category = models.CharField(verbose_name='カテゴリ',max_length=100, choices = CATEGORY_LINK, default='nihonuniv')
    logotype = models.BooleanField(verbose_name='横長true', default=True)
    
    class Meta:
       db_table = 'link_list'
       verbose_name = 'link_title'
       verbose_name_plural = 'link_content'
       
    def __str__(self):
        return self.title

############################################################################
class Book(models.Model):
    name = models.CharField(verbose_name='書籍名',max_length=150)
    pablisher = models.CharField(verbose_name='出版社',max_length=80,blank=True, null=True)
    ISBN = models.CharField(verbose_name='ISBN',max_length=20,blank=True, null=True)
    comment = CKEditor5Field(verbose_name='書籍紹介(書式は"Paragraph")',blank=True, null=True)
    thumbnail = models.ImageField(upload_to='book/', blank=True, null=True)
    url = models.URLField(verbose_name='書籍URL', help_text='基本的には出版元のURLを記載', blank=True, null=True)
    
    class Meta:
       db_table = 'book_list'
       verbose_name = 'book_title'
       verbose_name_plural = 'book_content'
       
    def __str__(self):
        return self.name

############################################################################
class WebBookmark(models.Model):
    name = models.CharField(verbose_name='名前',max_length=150)
    comment = CKEditor5Field(verbose_name='紹介文(書式は"Paragraph")',blank=True, null=True)
    url = models.URLField(verbose_name='URL')
    
    class Meta:
       db_table = 'web_list'
       verbose_name = 'web_title'
       verbose_name_plural = 'web_content'
       
    def __str__(self):
        return self.name