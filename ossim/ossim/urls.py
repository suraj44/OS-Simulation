
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('home.urls')),
    url(r'^sockets/',include('sockets.urls')),
    url(r'^synchro/',include('synchro.urls')),
    url(r'^file_allocation/',include('file_alloc.urls')),
    url(r'^deadlock/',include('deadlock.urls')),
    path('page/',include('page.urls')),
    path('disk/',include('disk_sched.urls')),
    path('process/',include('process.urls'))
]
