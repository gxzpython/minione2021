

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
# def index(request):
# 	return HttpResponse("Hello,world!😼")


from .models import Group,People,Event,NewUser

def login(request):
	# return HttpResponse("Hello,world!😼")
	template = loader.get_template('society/login.html')
	return HttpResponse(template.render({},request))

def index(request):
	template = loader.get_template('society/index.html')
	return HttpResponse(template.render({},request))


def group(request):
	group=Group.objects.all()
	template = loader.get_template('society/group.html')
	context = {
		'group':group,
	}
	return HttpResponse(template.render(context,request))

def event(request):
	event=Event.objects.all()
	template = loader.get_template('society/event.html')
	context = {
		'event':event,
	}
	return HttpResponse(template.render(context,request))


def people(request):
	people=People.objects.all()
	template = loader.get_template('society/people.html')
	context = {
		'people':people,
	}
	return HttpResponse(template.render(context,request))

def group_detail(request,group_id):
	group_detailview= Group.objects.get(id=group_id)
	template=loader.get_template('society/group_detail.html')
	context={
		'group_detailview':group_detailview
	}
	return HttpResponse(template.render(context,request))

def event_detail(request,event_id):
	event_detailview= Event.objects.get(id=event_id)
	template=loader.get_template('society/event_detail.html')
	context={
		'event_detailview':event_detailview
	}
	return HttpResponse(template.render(context,request))


def people_detail(request,people_id):
	people_detailview= People.objects.get(id=people_id)
	template=loader.get_template('society/people_detail.html')
	context={
		'people_detailview':people_detailview
	}
	return HttpResponse(template.render(context,request))




def success(request):
	# existing_user =NewUser.objects.all()
	
	# if NewUser.user_name in existing_user.existing_user:
	# 	template = loader.get_template('society/welcomeback.html')
	# 	context={
	# 		'existing_user':existing_user
	# 	}
	# 	return HttpResponse(template.render(context,request))
	# else:
	try:
		newuser= NewUser(user_name= request.POST["user_name"],
			pass_word=request.POST["pass_word"])
		newuser.save()

		if newuser.id is not None:
			template = loader.get_template('society/success.html')

			context={
				"message": "Success Registered",
				"user_id": newuser.id
			}
			return HttpResponse(template.render(context,request))
		else: 
			template = loader.get_template('society/success.html')
			return HttpResponse(template.render({"message":"User id error"},request))
	except Exception as error:
		template = loader.get_template('society/success.html')
		return HttpResponse(template.render({"message":"Opps !!! this user name has been used please use another username!!!"},request))
