from django.shortcuts import render, redirect

from .models import Employee
def index(request):
    return render(request, "index.html")


def Getdata(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    image = request.FILES["image"]

    save = Employee(idno=idno, name=name, salary=salary, image=image)
    save.save()
   #return render(request, "index.html", {"message": 'Employee Details saved successfully'})
    return redirect("/index/")

def EmployeedDetails(request):
    qs = Employee.objects.all()

    return render(request, "details.html", {"data": qs})


def delete(request):
    id = request.GET.get("idno")
    Employee.objects.filter(idno=id).delete()

    qs = Employee.objects.all()
    return render(request, "details.html", {"data": qs})


def update(request):
    idno = request.POST.get("idno")
    qs = Employee.objects.filter(idno=idno)

    return render(request, "update.html", {"data": qs})


def updateEmp(request):
    id = request.POST.get("idno")
    name = request.POST.get("name")
    sal = request.POST.get("salary")
    image = request.FILES["image"]
    save = Employee(idno=id, name=name, salary=sal, image=image)
    save.save()
    return render(request, "index.html", {"message": "Data Updated"})
