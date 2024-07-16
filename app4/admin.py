from django.contrib import admin
from app4.models import Course, Student 

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_usn', 'student_sem')
    ordering = ('student_name',)
    search_fields = ('student_name',)

admin.site.register(Course)
