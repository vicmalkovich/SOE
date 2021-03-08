from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from accounts.models import *


def home_view(request):
    context = {}
    if request.method == 'POST':
        phone_number_friend = request.POST.get('phone_number_friend')
        context['phone_number_friend'] = phone_number_friend


    return render(request, "System/home.html", context)

def adding_user_to_group_view(request, group_id):
    context = {}
    group = FriendsGroup.objects.get(id=group_id)
    
    
    if request.method == 'POST':
        input_user_id = request.POST.get('user_id')
        try:
            user_to_add = User.objects.get(id=input_user_id)
            group.users.add(user_to_add)
        except: 
            pass
    
    context['group'] = group
    context['users'] = group.users.all()
    
    return render(request, 'System/adding_users_to_group.html', context)


def delete_user_to_group_view(request, user_id, group_id):
    group = FriendsGroup.objects.get(id=group_id)
    user_to_remove = User.objects.get(id=user_id)
    group.users.remove(user_to_remove)

    return HttpResponseRedirect('/adding_user_to_group/'+ str(group_id) +'/')

def group_expenses_view(request, group_id):
    context={}
    group = FriendsGroup.objects.get(id=group_id)
    context['group'] = group
    

    return render(request, 'System/group_expenses.html', context)