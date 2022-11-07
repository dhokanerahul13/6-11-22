from django.shortcuts import render
from emp_app.models import employee,department,role
# Create your views here.
def index(request):
    return render(request,'emp_app/index.html')



def all_emp(request):
    emps=employee.objects.all()
    context={
        'emps':emps
    }
    print(emps)
    return render(request,'emp_app/all_emp.html',context)


def add_emp(request):
    return render(request,'emp_app/add_emp.html')


def remove_emp(request):
    return render(request,'emp_app/remove_emp.html')

def filter_emp(request):
    return render(request,'emp_app/filter_emp.html')  
        


