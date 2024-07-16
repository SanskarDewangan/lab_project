"""
URL configuration for lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app4.views import reg , course_search,add_project,StudentListView,StudentDetailView,construct_csv_from_model, construct_pdf_from_model2,regaj,course_search_ajax

admin.site.site_header="My Site Header" 
admin.site.site_title="My Site Title" 
admin.site.index_title="My Site Index"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', reg),
    path('course_search/',course_search),
    path('add_project/',add_project),
    path('student_list/', StudentListView.as_view()), 
    path('student_detail/<int:pk>/', StudentDetailView.as_view()),
    path('construct_course/', construct_csv_from_model),
    path('construct_pdf_from_model2/', construct_pdf_from_model2),
    path('regaj/',regaj),
    path('course_seacrh_ajax/',course_search_ajax),
]

