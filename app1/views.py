from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import register
def layout(request):
    return render(request,'layout.html')
def login(request):
    return render(request,'login.html')
def terms(request):
    return render(request,'terms.html')
def logincheck(request):
    email1=request.GET ['username']
    password1=request.GET ['password']
    try:
        r=register.objects.get(email=email1,password=password1)
        print("r=",r)
    except Exception as ex:
         return render(request,"login.html",{"msg":"invalid email/password"})
    if(r!=None):
        if(r.desig=='user'):
            return redirect('/recipe.html')
        if(r.desig=='admin'):
            return redirect('/viewuser.html')
        else:
             return render(request,"login.html",{"msg":"invalid designation"})
def recipe(request):
    return render(request,'recipe.html')
def reg(request):
    return render(request,'register.html')
def doregister(request): 
    email=request.GET['email']
    password=request.GET['psw'] 
    passwordrepeate=request.GET['psw-repeat']
    name=request.GET['name']
    gender=request.GET['gender']
    if register.objects.filter(email=email).exists():
            # Return an error if the email is already registered
            return render(request, "register.html", {"msg": "Email already exists, please use a different one."})
    r=register()
    r.email=email
    r.password=password
    r.repeatpassword=passwordrepeate
    r.name=name
    r.gender=gender
    r.save()
    return render(request,"login.html",{"msg":"registration sucessfull"})
def contact(request):
    return render(request,'contact.html')
def userhome(request):
    return render(request,'userhome.html')
def adminhome(request):
    return render(request,'adminhome.html')
def viewuser(request):
    users=register.objects.all
    return render(request,'viewuser.html',{"users":users})
def modify(request):
    operation=request.GET['operation']
    email=request.GET['email']
    password=request.GET['password']
    desig=request.GET['desig']
    name = request.GET['name']  
    gender = request.GET['gender']
    print(f"Name: {name}, Gender: {gender}")
    r=register.objects.get(email=email)
    if operation=="update":
        r.email=email
        r.password=password
        r.desig=desig
        r.name=name 
        r.gender=gender  
        r.save()
    else:
        register.delete(r)
    users=register.objects.all()
    print(operation)
    return render(request,"viewuser.html",{"users":users})
def pdf(request):
    return render(request,'pdf.html')


  

