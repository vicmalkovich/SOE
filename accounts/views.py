from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile
import random




def login_view(request):
    context = {}
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        sms_input = request.POST.get('sms')

        print('__________')
        if phone_number:
            if User.objects.get(username=phone_number):
                # UserProfile.objects.get_or_create(user=User.objects.get(username=phone_number), sms=random.randint(1000, 9999))
                context['phone_number'] = phone_number
    
                user_profile = UserProfile.objects.get(user=User.objects.get(username=phone_number))
                sms_get = user_profile.sms

           
                # sms_get = random.randint(1000, 9999) # RANDOM
                context['sms_get'] = sms_get
                if sms_input == sms_get:
                    print('hahhahha')
                    user = authenticate(username=User.objects.get(username=phone_number), password='1')
                    login(request, user)


    return render(request, "accounts/login.html", context)

