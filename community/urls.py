from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('articles/', views.index, name='index'),
    path('<int:article_pk>/articles/', views.pur_index, name='pur_index'),
    path('articles/index_search/', views.index_search, name='index_search'),
    path('articles/create/', views.create, name='create'),
    path('articles/<int:article_pk>/', views.detail, name='detail'),
    path("articles/<int:article_pk>/update", views.update, name="update"),
    path('articles/<int:article_pk>/delete/', views.delete, name='delete'),
    path('articles/<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),

]


