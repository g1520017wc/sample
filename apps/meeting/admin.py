from django.contrib import admin
from .models import Footer, MeetingCategory, Meeting, Presentation
from import_export import resources
from import_export.admin import ImportExportMixin, ImportExportModelAdmin, ExportActionModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

class FooterResorce(resources.ModelResource):
    footerkey = Field(attribute='footerkey', column_name='footerkey')
    body = Field(attribute='body', column_name='body')
    
    class Meta:
        model = Footer
        skip_unchanged = True
        use_bulk = True        

@admin.register(Footer)
class FooterAdmin(ImportExportModelAdmin):
    ordering = ['-footerkey']
    list_display = ('footerkey', 'body',)
    list_filter = ()
    resource_class = FooterResorce

##################################################################

class MeetingCategoryResource(resources.ModelResource):    
    name = Field(attribute='name', column_name='name')
    
    class Meta:
        model = MeetingCategory
        skip_unchanged = True
        use_bulk = True

@admin.register(MeetingCategory)
class MeetingCategoryAdmin(ImportExportModelAdmin):
    ordering = ['name']
    list_display = ('name',)
    resource_class = MeetingCategoryResource


##################################################################

class MeetingResorce(resources.ModelResource):
    key = Field(attribute='key', column_name='key')
    date = Field(attribute='date', column_name='date')
    category = Field(attribute='category', column_name='category', widget=ForeignKeyWidget(MeetingCategory, 'name'))
    style = Field(attribute='style', column_name='style')
    time = Field(attribute='time', column_name='time')
    times = Field(attribute='times', column_name='times')
    location = Field(attribute='location', column_name='location')
    theme = Field(attribute='theme', column_name='theme')
    joint = Field(attribute='joint', column_name='joint')
    application = Field(attribute='application', column_name='application', widget=ForeignKeyWidget(Footer, 'footerkey'))
    entrancefee = Field(attribute='entrancefee', column_name='entrancefee', widget=ForeignKeyWidget(Footer, 'footerkey'))
    friendship = Field(attribute='friendship', column_name='friendship', widget=ForeignKeyWidget(Footer, 'footerkey'))
    circular = Field(attribute='circular', column_name='circular', widget=ForeignKeyWidget(Footer, 'footerkey'))
    inquiry = Field(attribute='inquiry', column_name='inquiry', widget=ForeignKeyWidget(Footer, 'footerkey'))

    class Meta:
        model = Meeting
        skip_unchanged = True
        use_bulk = True        

@admin.register(Meeting)
class MeetingAdmin(ImportExportModelAdmin):
    ordering = ['-date','-key']
    list_display = ('key', 'date', 'category', 'style', 'time', 'times', 'location', 'theme', 'joint', 'application', 'entrancefee', 'friendship', 'circular', 'inquiry')
    resource_class = MeetingResorce

##################################################################

class PresentationResorce(resources.ModelResource):
    key = Field(attribute='key', column_name='key', widget=ForeignKeyWidget(Meeting, 'key'))
    title = Field(attribute='title', column_name='title')
    authors = Field(attribute='authors', column_name='authors')    
    time = Field(attribute='time', column_name='time')
    order = Field(attribute='order', column_name='order')
    prize = Field(attribute='prize', column_name='prize')
    file = Field(attribute='file', column_name='file')
    keyword1 = Field(attribute='keyword1', column_name='keyword1')
    keyword2 = Field(attribute='keyword2', column_name='keyword2')
    keyword3 = Field(attribute='keyword3', column_name='keyword3')
    keyword4 = Field(attribute='keyword4', column_name='keyword4')
    keyword5 = Field(attribute='keyword5', column_name='keyword5')

    class Meta:
        model = Presentation
        skip_unchanged = True
        use_bulk = True        

@admin.register(Presentation)
class PresentationAdmin(ImportExportModelAdmin):
    ordering = ['-key', 'order']
    list_display = ('key', 'title', 'authors', 'time', 'order', 'prize', 'file', 'keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5',)
    list_filter = ('key',)
    resource_class = PresentationResorce

