"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from user import views
from django.urls import include  # 导入include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.zhuce),
    path('ceshi2/', views.ceshi2),
    path('test_pic/', views.test_pic),
    path('change_my_local/<str:new_local>', views.change_my_local),
    path('change_my_job/<str:new_job>', views.change_my_job),
    path('change_my_xueli/<str:new_xueli>', views.change_my_xueli),
    path('company_info/<int:page_id>/', views.company_info),
    path('denglu/', views.denglu),
    path('zhuce/', views.zhuce),
    path('pie_bar_test', views.pie_bar_test),
    path('job_demand', views.job_demand),
    path('xinzi_bar', views.xinzi_bar),
    path('xinzi_predict', views.xinzi_predict),
]
