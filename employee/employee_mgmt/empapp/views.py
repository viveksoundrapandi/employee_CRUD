from django.shortcuts import render, redirect  
from datetime import datetime
from empapp.forms import EmployeeForm  
from empapp.models import Employee , WonDetails
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        emp = Employee()
        won = WonDetails()
        emp.eid = request.POST['eid']
        emp.ename = request.POST['ename']
        emp.status = request.POST['status']
        emp.start_date = datetime.strptime(request.POST['start_date'], "%Y/%m/%d").date()
        emp.end_date = datetime.strptime(request.POST['end_date'], "%Y/%m/%d").date()
        won.won_no = request.POST['won_no']
        won.won_name = request.POST['won_name']
        emp.won = won
        won.save()
        emp.save()
    return render(request,'index.html',{})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(eid=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    emp = Employee.objects.get(eid=id)  
    if request.method == "POST":  
        emp.eid = request.POST['eid']
        emp.ename = request.POST['ename']
        emp.status = request.POST['status']
        emp.start_date = datetime.strptime(request.POST['start_date'], "%Y/%m/%d").date()
        emp.end_date = datetime.strptime(request.POST['end_date'], "%Y/%m/%d").date()
        emp.won.won_no = request.POST['won_no']
        emp.won.won_name = request.POST['won_name']
        print "*************"
        print emp.won.won_name
        emp.won.save()
        emp.save()
    return render(request, 'edit.html', {'employee': emp})  
def destroy(request, id):  
    employee = Employee.objects.get(eid=id)  
    employee.delete()  
    return redirect("/show")  
