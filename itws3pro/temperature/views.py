from __future__ import unicode_literals
from .models import Temperature,Humidity,Moisture,WaterLevel 
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
context={}
def index(request):
	temp_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	temp_data=str(temp_data)	
	humi_data=Humidity.objects.all()[len(Humidity.objects.all())-1]
	humi_data=str(humi_data)
	mois_data=Moisture.objects.all()[len(Moisture.objects.all())-1]
	mois_data=str(mois_data)
	waterlevel_data=WaterLevel.objects.all()[len(WaterLevel.objects.all())-1]
	waterlevel_data=str(waterlevel_data)
	context={'temperature':temp_data,'humidity':humi_data,'moisture':mois_data,'waterlevel':waterlevel_data};
	return render(request,'temperature/home.html',context)
def getdata(request):
	if request.method=='GET' :
		temp_value=request.GET['temperature']
		humi_value=request.GET['humidity']
		mois_value=request.GET['moisture']
		waterlevel_value=request.GET['waterlevel']
		
		t_obj=Temperature()
		h_obj=Humidity()
		m_obj=Moisture()
		w_obj=WaterLevel()
		
		t_obj.tem_value=temp_value
		t_obj.save()
		h_obj.hum_value=humi_value
		h_obj.save()
		m_obj.moi_value=mois_value
		m_obj.save()
		
		w_obj.level_value=waterlevel_value
		w_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")
def temperature(request):
	temp_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	temp_data=str(temp_data)
	temp={'temperature':temp_data}	
	return render(request, 'temperature/Temperature.html',temp)

def humidity(request):
	humi_data=Humidity.objects.all()[len(Humidity.objects.all())-1]
	humi_data=str(humi_data)
	humi={'humidity':humi_data}	
	return render(request, 'temperature/Humidity.html',humi)

def soilmoist(request):
	mois_data=Moisture.objects.all()[len(Moisture.objects.all())-1]
	mois_data=str(mois_data)
	soil={'moist':mois_data}	
	return render(request, 'temperature/Soil.html',soil)

def waterlevel(request):
	waterlevel_data=WaterLevel.objects.all()[len(WaterLevel.objects.all())-1]
	waterlevel_data=str(waterlevel_data)
	level={'waterlevel':waterlevel_data}	
	return render(request, 'temperature/water.html',level)
	