
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from personal import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('about/',views.about,name = 'about'),
    path('blog/',include('blog.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls'))
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
