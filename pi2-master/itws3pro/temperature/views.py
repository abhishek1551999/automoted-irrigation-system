from __future__ import unicode_literals
from .models import Temperature,Plants
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .forms import plantForm
def index(request):

	temp_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	hum=str(temp_data.hum_value)
	tem=str(temp_data.tem_value)
	moist=str(temp_data.moist_value)
	lev=str(temp_data.lev_value)
	rain=str(temp_data.rain_value)
	temp2=[]
	for i in range(1,13):
		
		temp1_data=Temperature.objects.all()[len(Temperature.objects.all())-i]
		temp1_data=str(temp1_data.hum_value)
		temp1_data=float(temp1_data)
		temp2.append(temp1_data)
	temp3=[]
	for i in range(1,13):
		
		temp2_data=Temperature.objects.all()[len(Temperature.objects.all())-i]
		temp2_data=str(temp2_data.tem_value)
		temp2_data=float(temp2_data)
		temp3.append(temp2_data)
	temp4=[]
	for i in range(1,13):
		
		temp3_data=Temperature.objects.all()[len(Temperature.objects.all())-i]
		temp3_data=str(temp3_data.moist_value)
		temp3_data=float(temp3_data)
		temp4.append(temp3_data)

	
	context={'tem' : tem , 'hum' : hum,'moist' : moist , 'lev' : lev,'temp2':temp2,'temp3':temp3,'temp4':temp4,'rain':rain}
	return render(request,'temperature/index.html',context)
	
		

def getdata(request):
	if request.method=='GET' :
		temp_value=request.GET['temperature']
		temp_value1=request.GET['humidity']
		temp_value2=request.GET['moisture']
		temp_value3=request.GET['level']
		temp_value4=request.GET['rain']
		t_obj=Temperature()
		t_obj.tem_value=temp_value		
		t_obj.hum_value=temp_value1
		t_obj.moist_value=temp_value2		
		t_obj.lev_value=temp_value3
		t_obj.rain_value=temp_value4
		t_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")

def create(request):
	form = plantForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			pid = form.cleaned_data['pid']
			longitude = form.cleaned_data['longitude']
			latitude = form.cleaned_data['latitude']
			print(pid)
			print(longitude)
			print('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
			foo = Plants.objects.create(plant_id = int(pid),latitude = float(latitude), longitude = float(longitude))			
			return HttpResponseRedirect('/gen1')
		else:
			form = plantForm()
	return render(request,'temperature/new.html',{'form':form})



def general(request):
	return render(request, 'temperature/2.html' , {} )

def gen1(request):
	return render(request, 'temperature/3.html' , {} )
