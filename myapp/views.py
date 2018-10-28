from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from regshow import settings
from django.contrib.sessions.models import Session
from .models import *

def home(request):
    return render(request,'home.html')
def a(request):
    return render(request,'a.html')

def registration(request):
    if request.method=='POST':
        form1=userform(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            subject="Confirm Mail"
            msg="Dear Sir/Madam, Thank You"
            res= send_mail(subject,msg,settings.EMAIL_HOST_USER,[email])
            User.objects.create_user(username=username,
			first_name=first_name,last_name=last_name,
			email=email,password=password)			
            return HttpResponse('<h1>Thank You</h1>')
    else:
        form1=userform()
    return render(request,'registration.html',{'frm':form1})
	
def registration2(request):
    if request.method=='POST':
        form2=studentform(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponse('<h1>Thank You</h1>')
    else:
        form2=studentform()
    return render(request,'registration2.html',{'frm2':form2})
	
def login(request):
    return render(request,'login.html')
	
def check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)       
        return redirect('/display')
    else:
        return HttpResponse("<h1>Invalid</h1>") 
		
@login_required(login_url='/login')
def display(request):  
    abc = User.objects.all()
    return render(request,"display.html",{'emp':abc})

@login_required(login_url='/login')
def display2(request):  
    abc = Student.objects.all()
    return render(request,"display2.html",{'emp':abc})  		

def edit(request, id):  
    employee = User.objects.get(id=id) 	
    return render(request,'edit.html', {'employee':employee})
def edit2(request, id):  
    employee = Student.objects.get(id=id) 	
    return render(request,'edit2.html', {'employee':employee})	
	
def destroy(request, id):  
    employee = User.objects.get(id=id)  
    employee.delete()  
    return redirect("/display") 
def destroy2(request, id):  
    employee = Student.objects.get(id=id)  
    employee.delete()  
    return redirect("/display2")
	
def update(request, id):  
	employee = User.objects.get(id=id)  
	fo = userform(request.POST)
	print('A',fo)
	if fo.is_valid():
		print("B")
		form.save()          
		return redirect("/display")  
	return render(request, 'edit.html', {'employee': employee})
def update2(request, id):  
	employee = Student.objects.get(id=id)  
	form = studentform(request.POST, instance = employee)
	if form.is_valid():
		form.save()          
		return redirect("/display2")  
	return render(request, 'edit2.html', {'employee': employee})  	

def logout_user(request):
    logout(request)
    return redirect('/reg')
	
def search(request):
	print(request.method)
	if request.method =='POST':
		squery = request.POST['search_box1']
		if squery:
			s = User.objects.filter(first_name__icontains=squery) | User.objects.filter(email__icontains=squery)
			if s:
				return render(request,'search.html',{'q':s})
			else:
				return render(request,'notfound.html')        
		else:    
			return redirect('/')
	return HttpResponse("HEllo")		