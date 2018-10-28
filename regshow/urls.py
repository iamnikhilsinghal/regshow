from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
	path('',home),
	path('reg/',registration),
	path('reg2/',registration2),
	path('login',login),
	path('check',check),
	path('display',display),
	path('display2',display2),
	
	path('edit/<int:id>',edit),
	path('edit2/<int:id>',edit2), 
    path('update/<int:id>',update), 
    path('update2/<int:id>',update2),
    path('delete/<int:id>',destroy),
	path('delete2/<int:id>',destroy2),
	
	path('logout',logout_user),
	path('search',search),
]
