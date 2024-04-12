from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from telaLogin.models import Users
from django.contrib import messages

# junta os templates com as models

def home(request):
    if request.method == 'GET':
        return render(request, 'telaLogin/home.html')
    else:
        user = Users()
        user.email = request.POST.get('email')
        try:
            user.senha = int(request.POST.get('senha'))
        except: 
            messages.warning(request, 'Só pode ter números na senha')
            return HttpResponseRedirect('/')
        else:
            if Users.objects.filter(email = user.email).exists():
                if Users.objects.get(email = user.email).senha == user.senha:
                    messages.success(request, 'Usuário logado')
                    return HttpResponseRedirect('/')
                else:
                    messages.warning(request, 'Usuário não registrado ou senha não coincidente')
                    return HttpResponseRedirect('/')
            else:
                messages.warning(request, 'Usuário não registrado ou senha não coincidente')
                return HttpResponseRedirect('/')
    

def cadastro(request):

    if request.method == 'GET':
        return render(request, 'telaLogin/cadastro.html')
    else:
        
        user = Users()
        user.email = request.POST.get('email')

        if Users.objects.filter(email = user.email).exists():
            messages.warning(request, 'E-mail já cadastrado')
            return HttpResponseRedirect('cadastro')
        else:
            try:
                user.senha = int(request.POST.get('senha'))
                resenha = int(request.POST.get('resenha'))
            except ValueError:
                messages.warning(request, 'Só pode ter números na senha')
                return HttpResponseRedirect('cadastro')
            else:
                if user.senha != resenha:
                    messages.warning(request, 'As senhas não coincidem')
                    return HttpResponseRedirect('cadastro')    
                else:
                    user.save()
                    messages.success(request, 'Usuário cadastrado')
                    return HttpResponseRedirect('cadastro')

