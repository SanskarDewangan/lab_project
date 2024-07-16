from django.shortcuts import render , HttpResponse
from app4.models import Course,Student,ProjectReg
from django.views import generic
import csv
from reportlab.pdfgen import canvas

# Create your views here.

def reg(request): 
    if request.method == "POST": 
        sid=request.POST.get("sname") 
        cid=request.POST.get("cname") 
        student=Student.objects.get(id=sid) 
        course=Course.objects.get(id=cid) 
        res=student.enrolment.filter(id=cid) 
        if res: 
            return HttpResponse("<h1>Student already enrolled</h1>") 
        student.enrolment.add(course) 
        return HttpResponse("<h1>Student enrolled successfully</h1>") 
    else: 
        students=Student.objects.all() 
        courses=Course.objects.all()
        return render(request,"reg.html",{"students":students, "courses":courses})

def course_search(request): 
    if request.method=="POST":
        cid=request.POST.get("cname") 
        s=Student.objects.all() 
        student_list=list() 
        for student in s: 
            if student.enrolment.filter(id=cid): 
                student_list.append(student) 
        if len(student_list)==0: 
            return HttpResponse("<h1>No Students enrolled</h1>")
        return render(request,"selected_student.html",{"student_list":student_list})
    else: 
        courses=Course.objects.all() 
        return render(request,"course_search.html",{"courses":courses})

def add_project(request): 
    if request.method=="POST": 
        form=ProjectReg(request.POST) 
        if form.is_valid(): 
            form.save() 
            return HttpResponse("<h1>Record inserted successfully</h1>") 
        else: 
            return HttpResponse("<h1>Record not inserted</h1>") 
    else: 
        form=ProjectReg() 
        return render(request,"add_project.html",{"form":form})



class StudentListView(generic.ListView): 
    model=Student 
    template_name="student_list.html" 

class StudentDetailView(generic.DetailView): 
    model=Student 
    template_name="student_detail.html"

def construct_csv_from_model(request): 
    courses=Course.objects.all() 
    response=HttpResponse(content_type="text/csv") 
    response['Content-Disposition'] = 'attachment;filename="courses_data.csv"' 
    writer=csv.writer(response) 
    writer.writerow(["Course Name","Course Code","Credits"]) 
    for course in courses: 
      writer.writerow([course.course_name,course.course_code, course.course_credits]) 
    return response

def construct_pdf_from_model2(request): 
    courses=Course.objects.all() 
    response=HttpResponse(content_type="application/pdf") 
    response['Content-Disposition'] = 'attachment; filename="courses_data.pdf"' 
    c=canvas.Canvas(response) 
    c.drawString(70,720,"Course Name") 
    c.drawString(170,720,"Course Code") 
    c.drawString(270,720,"Credits") 
    y=660 
    for course in courses: 
        c.drawString(70,y,course.course_name) 
        c.drawString(170,y,course.course_code) 
        c.drawString(270,y,str(course.course_credits)) 
        y=y-60 
    c.showPage() 
    c.save() 
    return response


def regaj(request):
    if request.method == "POST": 
        sid=request.POST.get("sname") 
        cid=request.POST.get("cname") 
        student=Student.objects.get(id=sid) 
        course=Course.objects.get(id=cid) 
        res=student.enrolment.filter(id=cid) 
        if res: 
            return HttpResponse("<h1>Student already enrolled</h1>") 
        student.enrolment.add(course) 
        return HttpResponse("<h1>Student enrolled successfully</h1>") 
    else: students=Student.objects.all() 
    courses=Course.objects.all() 
    return render(request,"regaj.html",{"students":students, "courses":courses})

def course_search_ajax(request): 
    if request.method=="POST": 
        cid=request.POST.get("cname") 
        s=Student.objects.all() 
        student_list=list() 
        for student in s: 
            if student.enrolment.filter(id=cid): 
                student_list.append(student) 
        if len(student_list)==0: 
            return HttpResponse("<h1>No Students enrolled</h1>") 
        return render(request,"selected_students.html",{"student_list":student_list}) 
    else: 
        courses=Course.objects.all() 
        return render(request,"course_search_aj.html",{"courses":courses})



