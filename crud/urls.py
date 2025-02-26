"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from crud_app.views import crud_create_view, crud_list, crud_update_view, crud_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud_list, name="crud_list"),
    path('create/', crud_create_view.as_view(), name="crud_create"),
    path('update/<int:pk>', crud_update_view.as_view(), name="crud_update"),
    path('delete/<int:pk>', crud_delete_view.as_view(), name='crud_delete')
]
