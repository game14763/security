# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from login.models import Login

# Create your views here.
def LoginView(request):
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    else:
        return render(request, 'login.html')
    '''
    userlist = Login.objects.raw('SELECT * FROM login')
    status = 'Not Login'
    if request.method == 'POST':
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        account = Login.objects.raw("SELECT * FROM login WHERE username='" + input_username + "' AND password='" + input_password + "'")
        for i in account:
            status = "Login Success"
    my_dict = {'userlist': userlist, 'status': status}
    return render(request, 'login.html', context=my_dict)