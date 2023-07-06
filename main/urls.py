from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('stories/', views.stories, name="stories"),
    path('stories/<str:title>', views.story, name="story"),
    path('researches/', views.researches, name="researches"),
    path('articles/', views.articles, name="articles"),
    path('articles/<str:title>', views.article, name="article"),
    path('articles/<str:title>/<int:pk>/update/', views.update_comment, name='comment_update'),
    path('articles/<str:title>/<int:pk>/delete/', views.delete_comment, name='comment_delete'),
    path('resume/', views.resume, name="resume"),
    path('projects/', views.projects, name="projects"),

]
