from django.conf.urls import include,url
from . import views
urlpatterns = [
    url(r'^$', views.index ,name = "index") ,
    url(r'^get/$', views.getdata ,name ="get"),
	#url(r'^home/$', views.home, name = "home"),
	url(r'^tem/', views.temperature, name = "temperature"),
	url(r'^hem/',views.humidity,name="humidity"),
	url(r'^soil/',views.soilmoist,name="soilmoist"),
	url(r'^level/',views.waterlevel,name="waterlevel"),	
    #url(r'^temp/',views.temp),
]
