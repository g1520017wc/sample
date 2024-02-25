from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator  # インポート
from markdown import markdown  # 追加
from django_ckeditor_5.fields import CKEditor5Field


class Footer(models.Model):
    footerkey = models.CharField('フッターキー', max_length=50, help_text='フッターキーを入力してください．')
    body = CKEditor5Field('本文', help_text='本文を入力してください．(書式は"Paragraph")')
    
    class Meta:
        verbose_name_plural="研究会のフッターテーブル"
    
    def __str__(self):
        return self.footerkey

####################################################################################################################################################################################################################################

class MeetingCategory(models.Model):
    name = models.CharField(verbose_name='カテゴリ名',max_length=100)
    
    class Meta:
       db_table = 'meetingcategory_list'
       verbose_name = 'meetingcategory_name'
       verbose_name_plural = 'meetingcategory'
       
    def __str__(self):
        return self.name

####################################################################################################################################################################################################################################

class Meeting(models.Model):    
    key = models.CharField(verbose_name='研究会のキー', max_length=20, help_text='「西暦_回数」を入力してください.例：2022_2 (研究会以外の場合は「西暦_カテゴリ名」)')    
    date = models.DateField(verbose_name='日付')
    category = models.ForeignKey('MeetingCategory', on_delete=models.PROTECT, verbose_name="カテゴリ", related_name='meetingcategory', related_query_name='fmeetingcategory', default='1')
    style = models.IntegerField(verbose_name='表示スタイル', default='0', help_text='0:通常, 1:表彰有, 2:pdfスタイル', validators=[MinValueValidator(0), MaxValueValidator(2)])
    time = models.CharField(verbose_name='時間', max_length=20, default='13:00-17:00', help_text='時間を入力してください．例) 13:00-18:00', null=True, blank=True)
    times = models.IntegerField(verbose_name='回数', help_text='回数を入力してください．例：2', null=True, blank=True)
    location = CKEditor5Field(verbose_name='場所', help_text='開催する場所を入力してください．(書式は"Paragraph")', null=True, blank=True)
    theme = models.CharField(verbose_name='テーマ', max_length=150, help_text='テーマを入力してください.', null=True, blank=True)
    joint = CKEditor5Field(verbose_name='共催', help_text='共催を入力してください.(書式は"Paragraph")', null=True, blank=True)
    application = models.ForeignKey(Footer, on_delete = models.PROTECT, verbose_name='研究会参加申込', help_text='研究会参加の申込方法を入力してください．', null=True, blank=True, related_name='meetingapplication', related_query_name='fmeetingapplication')
    entrancefee = models.ForeignKey(Footer, on_delete = models.PROTECT, verbose_name='参加費', help_text='参加費を入力してください．', null=True, blank=True, related_name='meetingentrancefee', related_query_name='fmeetingentrancefee')
    friendship = CKEditor5Field(verbose_name='懇親会費', help_text='懇親会費を入力してください．(書式は"Paragraph")', null=True, blank=True)
    circular = models.ForeignKey(Footer, on_delete = models.PROTECT, verbose_name='会報', help_text='会報について入力してください．', null=True, blank=True, related_name='meetingcircular', related_query_name='fmeetingcircular')
    inquiry = models.ForeignKey(Footer, on_delete = models.PROTECT, verbose_name='問合せ先', help_text='問合せ先を入力してください．', null=True, blank=True, related_name='meetinginquiry', related_query_name='fmeetinginquiry')
    
    class Meta:
        db_table = 'meeting_list'
        verbose_name = 'meeting_name'
        verbose_name_plural="研究会テーブル"
    
    def __str__(self):
        return self.key


####################################################################################################################################################################################################################################
#presentation
class Presentation(models.Model):
    key = models.ForeignKey(Meeting, on_delete = models.PROTECT, verbose_name="研究会のキー", help_text='研究会のキーを選択してください．', related_name='presentation', related_query_name='fpresentation')
    title = CKEditor5Field('タイトル', help_text='講演のタイトルを入力してください．(段落の書式は「標準」が推奨)', null=True, blank=True)
    authors = CKEditor5Field(verbose_name='講演者と所属', default='〇山田 太郎（〇〇大学）', help_text='例) 〇山田 太郎（〇〇大学），山田 二郎（〇〇大学），発表者の前に〇をつける(書式は"Paragraph")', null=True, blank=True)
    time = models.CharField('時間', default='13:00-15:00', max_length=50, help_text='講演者の講演時間を入力してください．例：13:10-13:45', null=True, blank=True)
    order = models.IntegerField('順番', default='1', help_text='講演の順番を数字で入力してください．(休憩等も含む)', validators=[MinValueValidator(1), MaxValueValidator(20)])
    prize = models.BooleanField(verbose_name='鈴木・岡田記念賞', help_text='鈴木・岡田記念賞関連である場合True', default=False)
    file = models.FileField(verbose_name='pdfファイル', upload_to='meeting/', null=True, blank=True)
    keyword1 = models.CharField('キーワード1', max_length=100, help_text='キーワードを入力してください．', null=True, blank=True)
    keyword2 = models.CharField('キーワード2', max_length=100, help_text='キーワードを入力してください．', null=True, blank=True)
    keyword3 = models.CharField('キーワード3', max_length=100, help_text='キーワードを入力してください．', null=True, blank=True)
    keyword4 = models.CharField('キーワード4', max_length=100, help_text='キーワードを入力してください．', null=True, blank=True)
    keyword5 = models.CharField('キーワード5', max_length=100, help_text='キーワードを入力してください．', null=True, blank=True)
    
    class Meta:
        verbose_name_plural="講演テーブル"
    
    def Meeting(self):
        return self.key




