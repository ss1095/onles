"""
URL configuration for exam_system project.

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
from django.urls import path, include
from exam.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('exam/', include('exam.urls')),]
from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('create/', views.create_exam, name='create_exam'),
    path('<int:exam_id>/add-question/', views.add_question, name='add_question'),
    path('<int:exam_id>/', views.exam_details, name='exam_details'),
]
urlpatterns += [
    path('<int:exam_id>/take/', views.take_exam, name='take_exam'),
    path('<int:exam_id>/results/', views.exam_results, name='exam_results'),
]
urlpatterns += [
    path('performance-report/', views.performance_report, name='performance_report'),
]
urlpatterns += [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]


