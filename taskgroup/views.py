from django.shortcuts import render,redirect,render_to_response
from .forms import RegisterForm,LoginForm,TaskForm
from django.http import HttpResponseRedirect,HttpResponse
from .models import TaskModel,User
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			register = form.save(commit=False)
			pw = register.password
            # thus we need to use set password to encrypt the password string
			register.set_password(pw)
			register.save()
			register.save()
			registered = True
			return HttpResponseRedirect(reverse_lazy('taskgroup:tasklist'))
			#return HttpResponseRedirect("/")
	else:
		form = RegisterForm()
		return render(request, 'register.html', {'form' : form})

		
def login(request):
	print request.method
	records = TaskModel.objects.all()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			return render(request,'tasklist.html', {"records": records})
		else:
			return render(request, 'login.html',{'form': form})
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form' : form})


def task(request):
	user_data = User.objects.all()
	records = TaskModel.objects.all()
	return render(request,'tasklist.html', {"records": records}, {"user_data": user_data} ,)

def createtask(request):
	records = TaskModel.objects.all()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.save()
			return render(request,'tasklist.html', {"records": records})
		else:
			return render(request, 'createtask.html',{'form': form})
	else:		
		form = TaskForm()
		return render(request, 'createtask.html', {'form' : form})



def deletetask(request,tname):
	a = TaskModel.objects.filter(Status='completed')
	if a.first():
		records = TaskModel.objects.filter(id=tname)
		records.delete()
		return HttpResponseRedirect(reverse_lazy('taskgroup:tasklist'))
		#return HttpResponse('deleted')
	else:
		return HttpResponse('First compelete task')
def logout(request):
	return redirect('login.html')







