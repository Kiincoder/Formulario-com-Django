from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

#Form de cadastro do user
def create(request):
    return render(request, 'create.html')

#Insert dos dados
def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()

        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'


    return render(request, 'create.html', data)

#Formulário do painel de login
def painel(request):
    return render(request,'painel.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

#Página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

#logout do sistema
def logouts(request):
    logout(request)
    return render(request, 'home.html')

#Change password
# def changePassword(request):
#     user = User.objects.get(username=)
#     user.set_password('')
#     user.save()
#     logouts(request)
#     return redirect('/painel/')























