from django.conf.urls import include,url
from django.contrib import admin
#from temperature import views
urlpatterns = [
    url(r'^temperature/', include('temperature.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^',include('temperature.urls'))
    #url(r'^$',views.dashboard,name = "dashboard")
]