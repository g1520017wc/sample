from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'information'
urlcompE = 'hodic投稿・編集用ページ-kanjiみんなで編集/'

urlpatterns = [
    path('', views.schedule_view, name='information'),
    path('link/', views.link_view, name='link'),
    path('word/', views.word_view, name='word'),
    path('word/<str:wordname>/', views.explanation_view, name='explanation'),
    path('book/', views.book_view, name='book'),

############################################################################################

    #管理者関連
    #List関連

    #Conference
    path('conflist/' + urlcompE, views.conferecelist_view, name='conflist'),
    #Schedule
    path('schedulelist/' + urlcompE, views.schedulelist_view, name='schedulelist'),
    #WordCategory
    path('wordcategorylist/' + urlcompE, views.wordcategorylist_view, name='wordcategorylist'),
    #HoloWords
    path('holowordslist/' + urlcompE, views.holowordslist_view, name='holowordslist'),
    #Link
    path('linklist/' + urlcompE, views.linklist_view, name='linklist'),
    #Book
    path('booklist/' + urlcompE, views.booklist_view, name='booklist'),
    #WebBookmark
    path('webbookmarklist/' + urlcompE, views.webbookmarklist_view, name='webbookmarklist'),

############################################################################################

    #追加関連

    #Conference
    path('confregi/' + urlcompE, views.ConferenceCreateView.as_view(), name='confregi'),
    #Schedule
    path('scheduleregi/' + urlcompE, views.ScheduleCreateView.as_view(), name='scheduleregi'),
    #WordCategory
    path('wordcategoryregi/' + urlcompE, views.WordcategoryCreateView.as_view(), name='wordcategoryregi'),
    #HoloWords
    path('holowordsregi/' + urlcompE, views.HolowordsCreateView.as_view(), name='holowordsregi'),
    #Link
    path('linkregi/' + urlcompE, views.LinkCreateView.as_view(), name='linkregi'),
    #Book
    path('bookregi/' + urlcompE, views.BookCreateView.as_view(), name='bookregi'),
    #WebBookmark
    path('webbookmarkregi/' + urlcompE, views.WebbookmarkCreateView.as_view(), name='webbookmarkregi'),

############################################################################################

    #編集関連

    #Conference
    path('confedit/<int:pk>/' + urlcompE, views.ConferenceEditView.as_view(), name='confedit'),
    #Schedule
    path('scheduleedit/<int:pk>/' + urlcompE, views.ScheduleEditView.as_view(), name='scheduleedit'),
    #WordCategory
    path('wordcategoryedit/<int:pk>/' + urlcompE, views.WordcategoryEditView.as_view(), name='wordcategoryedit'),
    #HoloWords
    path('holowordsedit/<int:pk>/' + urlcompE, views.HolowordsEditView.as_view(), name='holowordsedit'),
    #Link
    path('linkedit/<int:pk>/' + urlcompE, views.LinkEditView.as_view(), name='linkedit'),
    #Book
    path('bookedit/<int:pk>/' + urlcompE, views.BookEditView.as_view(), name='bookedit'),
    #WebBookmark
    path('webbookmarkedit/<int:pk>/' + urlcompE, views.WebbookmarkEditView.as_view(), name='webbookmarkedit'),

############################################################################################

    #削除関連

    #Conference
    path('confdelete/<int:pk>/' + urlcompE, views.ConferenceDeleteView.as_view(), name='confdelete'),
    #Schedule
    path('scheduledelete/<int:pk>/' + urlcompE, views.ScheduleDeleteView.as_view(), name='scheduledelete'),
    #WordCategory
    path('wordcategorydelete/<int:pk>/' + urlcompE, views.WordcategoryDeleteView.as_view(), name='wordcategorydelete'),
    #HoloWords
    path('holowordsdelete/<int:pk>/' + urlcompE, views.HolowordsDeleteView.as_view(), name='holowordsdelete'),
    #Link
    path('linkdelete/<int:pk>/' + urlcompE, views.LinkDeleteView.as_view(), name='linkdelete'),
    #Book
    path('bookdelete/<int:pk>/' + urlcompE, views.BookDeleteView.as_view(), name='bookdelete'),
    #WebBookmark
    path('webbookmarkdelete/<int:pk>/' + urlcompE, views.WebbookmarkDeleteView.as_view(), name='webbookmarkdelete'),
]