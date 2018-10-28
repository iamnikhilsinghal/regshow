from django.conf import settings
from django.contrib.auth import logout
from django.http import *
from django.contrib.auth.models import User

import datetime 

class AutoLogout:
    def process_request(self, request):
        if request.user.is_authenticated():
            
            current_datetime = datetime.datetime.now()
            if 'last_login' in request.session :
                last = (current_datetime - request.session['last_login']).seconds
                if last > settings.SESSION_IDLE_TIMEOUT:
                    logout(request)
                    return HttpResponseRedirect('/')
            else:
                request.session['last_login']=current_datetime
        return None        
       
