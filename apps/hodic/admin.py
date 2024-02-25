from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from django.utils.safestring import mark_safe
from .models import UpdateModel, Circular, HodicCategory, HodicArticle, Manual
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget


class UpdateModelAdmin(ImportExportMixin, admin.ModelAdmin):
    model = UpdateModel
    list_display = ["date", "content", "link", "category"]
    list_filter = ["category"]
    ordering = ["-date"]
    
admin.site.register(UpdateModel, UpdateModelAdmin)

##################################################################

class CircularResource(resources.ModelResource):
    name = Field(attribute='name', column_name='theme_name')
    volume = Field(attribute='volume', column_name='volume')
    number = Field(attribute='number', column_name='number')
    date = Field(attribute='date', column_name='date')
    pdf = Field(attribute='pdf', column_name='pdf')
    toc = Field(attribute='toc', column_name='toc')
    
    class Meta:
        model = Circular
        skip_unchanged = True
        use_bulk = True
    
@admin.register(Circular)
# ImportExportModelAdminを継承したAdminクラスを作成する
class CircularAdmin(ImportExportModelAdmin):
    ordering = ['-date', '-number']
    list_display = ('name', 'volume', 'number', 'date', 'pdf', 'toc')
    # resource_classにModelResourceを継承したクラス設定
    resource_class = CircularResource

##################################################################

class HodicCategoryResource(resources.ModelResource):
    name = Field(attribute='name', column_name='name')
    
    class Meta:
        model = HodicCategory
        skip_unchanged = True
        use_bulk = True

@admin.register(HodicCategory)
class HodicCategoryAdmin(ImportExportModelAdmin):
    ordering = ['name']
    list_display = ('name',)
    resource_class = HodicCategoryResource

##################################################################

class HodicArticleResorce(resources.ModelResource):
    category = Field(attribute='category', column_name='category', widget=ForeignKeyWidget(HodicCategory, 'name'))
    subtitle = Field(attribute='subtitle', column_name='subtitle')
    order = Field(attribute='order', column_name='order')
    article = Field(attribute='article', column_name='article')

    class Meta:
        model = HodicArticle
        skip_unchanged = True
        use_bulk = True

@admin.register(HodicArticle)
class HodicArticleAdmin(ImportExportModelAdmin):
    list_filter = ["category"]
    ordering = ['category', 'order']
    list_display = ('category', 'subtitle', 'order', 'article')
    resource_class = HodicArticleResorce

##################################################################

class ManualResorce(resources.ModelResource):
    name = Field(attribute='name', column_name='name')
    category = Field(attribute='category', column_name='category')
    pdf = Field(attribute='pdf', column_name='pdf')
    
    class Meta:
        model = Manual
        skip_unchanged = True
        use_bulk = True

@admin.register(Manual)
class ManualAdmin(ImportExportModelAdmin):
    ordering = ['name']
    list_display = ('name', 'category', 'pdf')
    resource_class = ManualResorce
