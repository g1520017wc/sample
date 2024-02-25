from django.urls import path
from . import views

app_name = 'hodic'
urlcompE = 'hodic投稿・編集用ページ-kanjiみんなで編集/'


urlpatterns = [
    path('', views.HodicView.as_view(), name='hodic'),
    path('about/', views.AboutView, name='about'),
    path('nyukai/', views.NyukaiView, name='nyukai'),
    
    #circular関連
    path('circular/', views.CircularView, name='circular'),
    path('toc/<int:volume>/', views.TOCView, name='toc'),
    
    #管理者関連
    #list表示
    path('updatelist/' + urlcompE, views.updatelist_view, name='updatelist'),
    path('circularlist/' + urlcompE, views.circularlist_view, name='circularlist'),
    path('hodiccategorylist/' + urlcompE, views.hodiccategorylist_view, name='hodiccategorylist'),
    path('hodicarticlelist/' + urlcompE, views.hodicarticlelist_view, name='hodicarticlelist'),
    #追加
    path('updateregi/' + urlcompE, views.UpdateCreateView.as_view(), name='updateregi'),
    path('circularregi/' + urlcompE, views.CircularCreateView.as_view(), name='circularregi'),
    path('hodiccategoryregi/' + urlcompE, views.HodiccategoryCreateView.as_view(), name='hodiccategoryregi'),
    path('hodicarticleregi/' + urlcompE, views.HodicarticleCreateView.as_view(), name='hodicarticleregi'),
    #編集
    path('updateedit/<int:pk>/' + urlcompE, views.UpdateEditView.as_view(), name='updateedit'),
    path('circularedit/<int:pk>/' + urlcompE, views.CircularEditView.as_view(), name='circularedit'),
    path('hodiccategoryedit/<int:pk>/' + urlcompE, views.HodiccategoryEditView.as_view(), name='hodiccategoryedit'),
    path('hodicarticleedit/<int:pk>/' + urlcompE, views.HodicarticleEditView.as_view(), name='hodicarticleedit'),
    #削除
    path('updatedelete/<int:pk>/' + urlcompE, views.UpdateDeleteView.as_view(), name='updatedelete'),
    path('circulardelete/<int:pk>/' + urlcompE, views.CircularDeleteView.as_view(), name='circulardelete'),
    path('hodiccategorydelete/<int:pk>/' + urlcompE, views.HodiccategoryDeleteView.as_view(), name='hodiccategorydelete'),
    path('hodicarticledelete/<int:pk>/' + urlcompE, views.HodicarticleDeleteView.as_view(), name='hodicarticledelete'),
    #マニュアル
    path('manuallist/' + urlcompE, views.manuallist_view, name='manuallist'),
    path('manual/' + urlcompE, views.manual_view, name='manual'),
]