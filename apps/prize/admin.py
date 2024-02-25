from django.contrib import admin
from .models import SpModel, YearModel, SuzukiokadaModel, ArticleModel, Studentaward
from import_export import resources
from import_export.admin import ImportExportMixin, ImportExportModelAdmin, ExportActionModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from django.utils.safestring import mark_safe

class YearResorce(resources.ModelResource):
    AD = Field(attribute='AD', column_name='AD')
    year = Field(attribute='year', column_name='year')
    prize_type = Field(attribute='prize_type', column_name='prize_type')
    prizekey = Field(attribute='prizekey', column_name='prizekey')
    times = Field(attribute='times', column_name='times')
    chairman = Field(attribute='chairman', column_name='chairman')

    class Meta:
        model = YearModel
        skip_unchanged = True
        use_bulk = True        

@admin.register(YearModel)
class YearModelAdmin(ImportExportModelAdmin):
    ordering = ['-AD']
    list_display = ('AD', 'year', 'prize_type', 'prizekey', 'times', 'chairman')
    list_filter = ('AD', 'prize_type')
    resource_class = YearResorce

#############################################################################
class SuzukiokadaResorce(resources.ModelResource):
    prizekey = Field(attribute='prizekey', column_name='prizekey', widget=ForeignKeyWidget(YearModel, 'prizekey'))
    kind = Field(attribute='kind', column_name='kind')  
    name = Field(attribute='name', column_name='name')
    affiliation = Field(attribute='affiliation', column_name='affiliation')

    class Meta:
        model = SuzukiokadaModel
        skip_unchanged = True
        use_bulk = True

@admin.register(SuzukiokadaModel)
class SuzukiokadaModelAdmin(ImportExportModelAdmin):
    ordering = ['prizekey']
    list_display = ('prizekey', 'kind', 'name', 'affiliation')
    resource_class  = SuzukiokadaResorce

#############################################################################
class ArticleModelResorce(resources.ModelResource):
    prizekey = Field(attribute='prizekey', column_name='prizekey', widget=ForeignKeyWidget(YearModel, 'prizekey'))
    article_style = Field(attribute='article_style', column_name='article_style')
    pdf = Field(attribute='pdf', column_name='pdf')
    article = Field(attribute='article', column_name='article')

    class Meta:
        model = ArticleModel
        skip_unchanged = True
        use_bulk = True        

@admin.register(ArticleModel)
class ArticleModelAdmin(ImportExportModelAdmin):
    ordering = ['-prizekey']
    list_display = ("prizekey", "article_style", "pdf", "article")    
    resource_class = ArticleModelResorce

#############################################################################
class StudentawardResorce(resources.ModelResource):
    prizekey = Field(attribute='prizekey', column_name='prizekey', widget=ForeignKeyWidget(YearModel, 'prizekey'))
    title = Field(attribute='title', column_name='title')  
    name = Field(attribute='name', column_name='name')

    class Meta:
        model = Studentaward
        skip_unchanged = True
        use_bulk = True

@admin.register(Studentaward)
class StudentawardAdmin(ImportExportModelAdmin):
    ordering = ['prizekey']
    list_display = ('prizekey', 'title', 'name')
    resource_class  = StudentawardResorce
    
#############################################################################
class SpModelResorce(resources.ModelResource):
    name = Field(attribute='name', column_name='name')
    affiliation = Field(attribute='affiliation', column_name='affiliation')      
    date = Field(attribute='date', column_name='date')  
    text = Field(attribute='text', column_name='text')
    
    class Meta:
        model = SpModel
        skip_unchanged = True
        use_bulk = True

@admin.register(SpModel)
class SpModelawardAdmin(ImportExportModelAdmin):
    ordering = ['date']
    list_display = ('name', 'affiliation', 'date', 'text')
    resource_class  = SpModelResorce
    
    
    
    