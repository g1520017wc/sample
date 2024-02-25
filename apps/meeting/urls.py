from django.urls import path
from . import views

app_name = "meeting"
urlcompE = 'hodic投稿・編集用ページ-kanjiみんなで編集/'

urlpatterns = [
    
    #管理者関連
    #list表示
    path('meetinglist/' + urlcompE, views.meetinglist_view, name='meetinglist'),
    path('presenlist/<str:meetingkey>/' + urlcompE, views.presenlist_view, name='presenlist'),
    path('footerlist/' + urlcompE, views.footerlist_view, name='footerlist'),
    path('meetingcategorylist/' + urlcompE, views.meetingcategorylist_view, name='meetingcategorylist'),
    #追加
    path('meetingregi' + urlcompE, views.MeetingCreateView.as_view(), name='meetingregi'),
    path('presenregi/<str:meetingkey>/' + urlcompE, views.PresenCreateView.as_view(), name='presenregi'),
    path('footerregi' + urlcompE, views.FooterCreateView.as_view(), name='footerregi'),
    path('meetingcategoryregi' + urlcompE, views.MeetingcategoryCreateView.as_view(), name='meetingcategoryregi'),
    #編集
    path('meetingedit/<int:pk>/' + urlcompE, views.MeetingEditView.as_view(), name='meetingedit'),
    path('presenedit/<int:pk>/<str:meetingkey>/' + urlcompE, views.PresenEditView.as_view(), name='presenedit'),
    path('footeredit/<int:pk>/' + urlcompE, views.FooterEditView.as_view(), name='footeredit'),
    path('meetingcategoryedit/<int:pk>/' + urlcompE, views.MeetingcategoryEditView.as_view(), name='meetingcategoryedit'),
    #削除
    path('meetingdelete/<int:pk>/' + urlcompE, views.MeetingDeleteView.as_view(), name='meetingdelete'),
    path('presendelete/<int:pk>/<str:meetingkey>/' + urlcompE, views.PresenDeleteView.as_view(), name='presendelete'),
    path('footerdelete/<int:pk>/' + urlcompE, views.FooterDeleteView.as_view(), name='footerdelete'),
    path('meetingcategorydelete/<int:pk>/' + urlcompE, views.MeetingcategoryDeleteView.as_view(), name='meetingcategorydelete'),
    
    
#####################################################################################################################
    
    
    path("", views.meeting_view, name="meeting"),
    path('<str:detailkey>/', views.DetailView, name='detail'),
    
    
]


