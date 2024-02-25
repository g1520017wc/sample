from django.contrib import admin
from .models import Conference, Schedule, Link, WordCategory, HoloWords, Book, WebBookmark
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

# Register your models here.

class ConferenceResource(resources.ModelResource):
    name = Field(attribute='name', column_name='name')
    name_ja = Field(attribute='name_ja', column_name='name_ja')
    name_en = Field(attribute='name_en', column_name='name_en')
    period_disp = Field(attribute='period_disp', column_name='period_disp')
    period = Field(attribute='period', column_name='period')
    url = Field(attribute='url', column_name='url')
    display = Field(attribute='display', column_name='display')
    
    class Meta:
        model = Conference
        skip_unchanged = True
        use_bulk = True
    
@admin.register(Conference)
# ImportExportModelAdminを継承したAdminクラスを作成する
class ConferenceAdmin(ImportExportModelAdmin):
    ordering = ['period']
    list_display = ('name', 'name_ja', 'name_en', 'period_disp', 'period', 'url', 'display')
    # resource_classにModelResourceを継承したクラス設定
    resource_class = ConferenceResource

##################################################################

class ScheduleResource(resources.ModelResource):
    name = Field(attribute='name', column_name='name', widget=ForeignKeyWidget(Conference, 'name'))
    opendate = Field(attribute='opendate', column_name='opendate')
    closedate = Field(attribute='closedate', column_name='closedate')
    deadline = Field(attribute='deadline', column_name='deadline')
    url = Field(attribute='url', column_name='url')
    
    class Meta:
        model = Schedule
        skip_unchanged = True
        use_bulk = True
    
@admin.register(Schedule)
# ImportExportModelAdminを継承したAdminクラスを作成する
class ScheduleAdmin(ImportExportModelAdmin):
    ordering = ['opendate']
    list_display = ('name', 'opendate', 'closedate', 'deadline', 'url')
    # resource_classにModelResourceを継承したクラス設定
    resource_class = ScheduleResource

##################################################################

class LinkResource(resources.ModelResource):    
    title = Field(attribute='title', column_name='title')
    order = Field(attribute='order', column_name='order')
    introduction = Field(attribute='introduction', column_name='introduction')
    thumbnail = Field(attribute='thumbnail', column_name='thumbnail')
    url = Field(attribute='url', column_name='url')
    category = Field(attribute='category', column_name='category')
    logotype = Field(attribute='logotype', column_name='logotype')
    
    class Meta:
        model = Link
        skip_unchanged = True
        use_bulk = True
       
@admin.register(Link)
# ImportExportModelAdminを継承したAdminクラスを作成する
class LinkAdmin(ImportExportModelAdmin):
    ordering = ['order']
    list_display = ('title', 'order', 'introduction', 'thumbnail', 'url', 'category', 'logotype')
    # resource_classにModelResourceを継承したクラス設定
    resource_class = LinkResource

##################################################################

class WordCategoryResource(resources.ModelResource):    
    name = Field(attribute='name', column_name='name')
    
    class Meta:
        model = WordCategory
        skip_unchanged = True
        use_bulk = True

@admin.register(WordCategory)
# ImportExportModelAdminを継承したAdminクラスを作成する
class WordCategoryAdmin(ImportExportModelAdmin):
    ordering = ['name']
    list_display = ('name',)
    # resource_classにModelResourceを継承したクラス設定
    resource_class = WordCategoryResource

##################################################################

class HoloWordsResource(resources.ModelResource):    
    wordname = Field(attribute='wordname', column_name='wordname')
    wordename = Field(attribute='wordename', column_name='wordename')
    abbreviation = Field(attribute='abbreviation', column_name='abbreviation')
    category = Field(attribute='category', column_name='category')
    article = Field(attribute='article', column_name='article')
    display = Field(attribute='display', column_name='display')
    
    class Meta:
        model = HoloWords
        skip_unchanged = True
        use_bulk = True
       
@admin.register(HoloWords)
# ImportExportModelAdminを継承したAdminクラスを作成する
class HoloWordsAdmin(ImportExportModelAdmin):
    ordering = ['wordname']
    list_display = ('wordname', 'wordename', 'abbreviation', 'category', 'article', 'display')
    # resource_classにModelResourceを継承したクラス設定
    resource_class = HoloWordsResource

##################################################################

class BookResource(resources.ModelResource):    
    name = Field(attribute='name', column_name='name')
    pablisher = Field(attribute='pablisher', column_name='pablisher')
    ISBN = Field(attribute='ISBN', column_name='ISBN')
    comment = Field(attribute='comment', column_name='comment')
    thumbnail = Field(attribute='thumbnail', column_name='thumbnail')
    url = Field(attribute='url', column_name='url')
    
    class Meta:
        model = Book
        skip_unchanged = True
        use_bulk = True

@admin.register(Book)
# ImportExportModelAdminを継承したAdminクラスを作成する
class BookAdmin(ImportExportModelAdmin):
    ordering = ['name']
    list_display = ('name', 'pablisher', 'ISBN', 'comment', 'thumbnail', 'url')
    # resource_classにModelResourceを継承したクラス設定
    resource_class = BookResource

##################################################################

class WebBookmarkResource(resources.ModelResource):    
    name = Field(attribute='name', column_name='name')
    comment = Field(attribute='comment', column_name='comment')
    url = Field(attribute='url', column_name='url')
    
    class Meta:
        model = WebBookmark
        skip_unchanged = True
        use_bulk = True

@admin.register(WebBookmark)
# ImportExportModelAdminを継承したAdminクラスを作成する
class WebBookmarkAdmin(ImportExportModelAdmin):
    ordering = ['name']
    list_display = ('name', 'comment', 'url')
    # resource_classにModelResourceを継承したクラス設定
    resource_class = WebBookmarkResource











