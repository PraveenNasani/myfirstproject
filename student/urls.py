from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='index' ),
    path('second/',views.second ),
    path('html/',views.html_file ),
    path('dynamic/',views.dynamic_html ),
    path('details/',views.student_details),
    path('student_form/',views.student_form,name='student_form'),
    path('students_list/',views.students_list),
]
