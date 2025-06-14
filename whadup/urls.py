from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings # This is the main URL configuration for the Django project.
from articles import views as articles_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('about/', views.about),
    path('', articles_views.article_list, name='home'),  # Redirects to the article list view
]

urlpatterns += staticfiles_urlpatterns() # This line is used to serve static files during development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    