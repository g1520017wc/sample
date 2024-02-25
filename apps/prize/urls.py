from django.urls import path
from . import views

app_name = "prize"
urlcompE = 'hodic投稿・編集用ページ-kanjiみんなで編集/'

urlpatterns = [

    #管理者関連
    #list表示
    
    #特別賞
    path('splist/' + urlcompE, views.splist_view, name='splist'),
    #学生賞
    path('studentlist/' + urlcompE, views.studentlist_view, name='studentlist'),
    #HODIC賞
    path('prizelist/' + urlcompE, views.prizelist_view, name='prizelist'),
    #鈴木・岡田記念賞の記事
    path('articlelist/' + urlcompE, views.articlelist_view, name='articlelist'),
    #鈴木・岡田記念賞の受賞者
    path('prizewinnerlist/' + urlcompE, views.prizewinnerlist_view, name='prizewinnerlist'),

########################################################################################

    #追加
    
    #特別賞
    path('spregi' + urlcompE, views.SpCreateView.as_view(), name='spregi'),
    #学生賞
    path('studentregi' + urlcompE, views.StudentCreateView.as_view(), name='studentregi'),
    #HODIC賞
    path('prizeregi' + urlcompE, views.PrizeCreateView.as_view(), name='prizeregi'),
    #鈴木・岡田記念賞の記事
    path('articleregi' + urlcompE, views.ArticleCreateView.as_view(), name='articleregi'),
    #鈴木・岡田記念賞の受賞者
    path('prizewinnerregi' + urlcompE, views.PrizewinnerCreateView.as_view(), name='prizewinnerregi'),

########################################################################################

    #編集
    
    #特別賞
    path('spedit/<int:pk>/' + urlcompE, views.SpEditView.as_view(), name='spedit'),
    #学生賞
    path('studentedit/<int:pk>/' + urlcompE, views.StudentEditView.as_view(), name='studentedit'),
    #HODIC賞
    path('prizeedit/<int:pk>/' + urlcompE, views.PrizeEditView.as_view(), name='prizeedit'),
    #鈴木・岡田記念賞の記事
    path('articleedit/<int:pk>/' + urlcompE, views.ArticleEditView.as_view(), name='articleedit'),
    #鈴木・岡田記念賞の受賞者
    path('prizewinneredit/<int:pk>/' + urlcompE, views.PrizewinnerEditView.as_view(), name='prizewinneredit'),

########################################################################################

    #削除
    
    #特別賞
    path('spdelete/<int:pk>/' + urlcompE, views.SpDeleteView.as_view(), name='spdelete'),
    #学生賞
    path('studentdelete/<int:pk>/' + urlcompE, views.StudentDeleteView.as_view(), name='studentdelete'),
    #HODIC賞
    path('prizedelete/<int:pk>/', views.PrizeDeleteView.as_view(), name='prizedelete'),
    #鈴木・岡田記念賞の記事
    path('articledelete/<int:pk>/' + urlcompE, views.ArticleDeleteView.as_view(), name='articledelete'),
    #鈴木・岡田記念賞の受賞者
    path('prizewinnerdelete/<int:pk>/' + urlcompE, views.PrizewinnerDeleteView.as_view(), name='prizewinnerdelete'),


############################################################################################

    path("", views.PrizeView, name="prize"),
    path("sp", views.SpView.as_view(), name="sp"),
    path("commemorative", views.CommemorativeView.as_view(), name="commemorative"),
    path("commemorative/<str:articlekey>/", views.ArticleView, name="article"),
    path("excellence", views.ExcellenceView, name="excellence"),
    path("symposium", views.SymposiumView, name="symposium"),

]


























