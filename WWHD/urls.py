"""WWHD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import WWHDapp.views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WWHDapp.views.main, name='main'),
    path('brand/',WWHDapp.views.brand, name = 'brand'),
    path('update/<int:update_id>', WWHDapp.views.update, name='update'),
    path('create/', WWHDapp.views.create, name ='create'),
    path('delete/<int:delete_id>', WWHDapp.views.delete, name ='delete'),
    path('incategory/<int:category_id>',WWHDapp.views.incategory, name = 'incategory'),
    path('search/',WWHDapp.views.searchResult, name = 'searchResult'),
    path('detail/<int:detail_id>',WWHDapp.views.detail, name='detail'),
    path('login/', WWHDapp.views.login, name='login'),
    path('signup/', WWHDapp.views.signup, name='signup'),
    path('logout/', WWHDapp.views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
