from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import StudentData
from .forms import StudentForm
from django.db.models import Sum
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def index(request):
    return HttpResponse('Heyy,its my first django project')

def second(request):
    return HttpResponse('<h2>Hey i am second line</h2>')

def html_file(request):
    return render(request,'html_file.html')
#@html_file
def dynamic_html(request):
    context={'name':'Rahul','age':23}
    return render(request,'dynamic_html.html',context)

def student_details(request):
    x=StudentData.objects.all()
    return render(request,'student_details.html',context={'details':x})
#total=StudentData.objects.aggregate(Sum('grade'))
#print(total)
def students_list(request):
    details=[]
    count=[]
    sum_rollno_list=[]
    new_list=[]
    for i in range(1,11):
        x=StudentData.objects.all().filter(grade=i)
        sum_rollno=StudentData.objects.filter(grade=i).aggregate(Sum('rollno'))
        sum_rollno_list.append(sum_rollno)
        details.append(x)
        count.append(i)
        temp=[]
        temp.append(x)
        temp.append(sum_rollno)
        temp.append(i)
        new_list.append(temp)
    print(new_list)
    return render(request,'students_list.html',context={'details':details,'count':count,'sum_rollno':sum_rollno_list,'new_list':new_list})
    #print(x)

def student_form(request):
    if request.method=='POST':
        student_form=StudentForm(data=request.POST)
        if student_form.is_valid():
            fname=student_form.cleaned_data['fname']
            student=student_form.save()
            student.save()
            #student_form=StudentForm()
            return render(request,'success.html',context={'fname':fname})
        else:
            print('Please enter all details properly')
            #student_form=StudentForm()
    else:
        student_form = StudentForm()
    return render(request,'studentform.html',context={'student_form':student_form})
