from django.urls import path,include
from .import views
app_name = 'blog'
urlpatterns = [
    path('',views.blog,name = 'blog'),
    path('<int:blog_id>/',views.detail,name = 'detail'),
]
