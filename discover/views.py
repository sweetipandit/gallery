from django.shortcuts import render,redirect

# Create your views here.

from .models import ImageModel
from .models import RegistrationModel

#from django.http import HttpResponseRedirect
from django.contrib import messages

from django.db.models import Q
from django.contrib.sessions.models import Session

#from .models import UserRegister
#from .models import OrganizerDetail



def index(request):
	if request.session.has_key('user'):
		user_contact=request.session['user']
		userobj=RegistrationModel.objects.filter(userContact__exact=user_contact)
		image=ImageModel.objects.filter(user=userobj[0])
		context={'image':image,'userobj':userobj}
		return render(request,'discover/profile.html',context)
	else:
		return render(request,'discover/index.html')

	

		

	
def registration(request):
	return render(request,'discover/user_registration.html')
	

def login(request):
	return render(request,'discover/user_login.html')


def logout(request):
	del request.session['user']
	return redirect('index')











def upload(request,regUser_id):
	if request.method == 'POST':
		
		user_image=request.FILES['image']
		user_image_title=request.POST['title']

		userReg=RegistrationModel.objects.get(pk=regUser_id)
		image_upload=ImageModel(userImage=user_image,titele=user_image_title,user=userReg)
		image_upload.save()
		
		image=ImageModel.objects.filter(user=userReg)
		context={'image':image}

		return render(request,'discover/after_upload.html',context)
		
			
			
		
	else:
		return render(request,'discover/profile.html')

	











def submitRegistration(request):
	if request.method == 'POST':
		user_name=request.POST['user_name']
		user_contact=request.POST['user_contact']
		user_email=request.POST['user_email']
		user_password=request.POST['user_password']
		user_conform_password=request.POST['user_conform_password']
		if user_password == user_conform_password:
			register=RegistrationModel(userName=user_name,userContact=user_contact,userEmailId=user_email,userPassword=user_password)
			register.save()
			return render(request,'discover/successfully_registration.html')
		
		else:
			return render(request,'discover/user_registration.html')
			
			
		
	else:
		return render(request,'discover/user_registration.html')








							

def submitLogin(request):
	if request.method == 'POST':
		user_contact=request.POST['user_contact']
		user_password=request.POST['user_password']
		    
		
		userobj=RegistrationModel.objects.filter(userContact__exact=user_contact,  userPassword__exact=user_password)
		
		if userobj:
			request.session['user']=user_contact
			image=ImageModel.objects.filter(user=userobj[0])

			context={'image':image,'userobj':userobj}
		
			return render(request,'discover/profile.html',context)
		else:

			msg=messages.error(request,'user is not valid please register first or if your registration done fill correct user name and password')
			context={'msg':msg}
			return render(request,'discover/incurrect_login.html',context)

	else: 
		return HttpResponseRedirect(request,'discover/user_login.html')
		
		










def search(request):
	if request.method == 'POST':
		srch = request.POST['srh']

		if srch:
			match = ImageModel.objects.filter(Q(titele__icontains=srch))


			if match:
				return render(request, 'discover/profile.html',{'sr':match})
			else:
				messages.error(request,'no result found')

		else:
			return HttpResponseRedirect('/search/')

	return render(request,'discover/profile.html')		


