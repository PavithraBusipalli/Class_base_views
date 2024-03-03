"""
URL configuration for CBV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun_str_res/',fun_str_res,name='fun_str_res'),
    path('Cls_str_res/',Cls_str_res.as_view(),name='Cls_str_res'),
    path('fun_rend_temp/',fun_rend_temp,name='fun_rend_temp'),
    path('Cls_rend_temp/',Cls_rend_temp.as_view(),name='Cls_rend_temp'),
    path('Cls_spec_temp/',Cls_spec_temp.as_view(),name='Cls_spec_temp'),
    path('fun_Scl_form/',fun_Scl_form,name='fun_Scl_form'),
    path('Cls_gen_Form/',Cls_gen_Form.as_view(),name='Cls_gen_Form'),
    path('Cls_Spec_SclForm/',Cls_Spec_SclForm.as_view(),name='Cls_Spec_SclForm')
]

