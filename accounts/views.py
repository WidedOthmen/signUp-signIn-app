from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import UserForm
from rest_framework.decorators import api_view

from accounts.models import User

@csrf_exempt
@api_view(["POST"])
def registration(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('hell yeah')
        return HttpResponse('hell Noo!')
    return HttpResponse('random shit')


@api_view(["POST"])
def login(request):
    email = request.data["email"]
    password = request.data['password']
    if request.method == 'POST':
        try:
            a = User.objects.get(email = email, password= password) #select * from accounts_user where email ='hjjj' and password='hkkh'
            print(a.email)
        except User.DoesNotExist:
            return HttpResponse('user does not exist')
    return HttpResponse('shit')