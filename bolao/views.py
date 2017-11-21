from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApostaForm
from bolao.forms import (
	RegistrationForm,
	EditarPerfilForm
)
from .models import Partida, selecao, aposta
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# from django.forms.widgets import HiddenInput
from django.contrib.auth.decorators import login_required

def listaposta(request, partida):
	ap = aposta.objects.all()
	p = Partida.objects.get(id=partida)
	args = {'ap': ap, 'partida': p}
	return render(request, 'lista_apostas.html', args)

def apostar(request, partida=None):
	if request.method == 'POST':
		form = ApostaForm(request.POST)
		if form.is_valid():
			p = Partida.objects.get(id=partida)
			u = request.user
			aposta = form.save(commit=False)
			aposta.aposta_partida = p
			aposta.usuario = u
			aposta.save()
			return redirect('/bolao')
		else:
			return HttpResponse("Erro 404")
	else:
		if partida:
			p = Partida.objects.get(id=partida) #P = PE Pedro VS LU Lucas
			form = ApostaForm() # CHAMANDO O FORMULÁRIO
			#form.fields['aposta_partida'].widget = HiddenInput() # ESCONDENDO O CAMPO APOSTA_PARTIDA
			# aposta.aposta_partida = p
			#del form.fields['aposta_partida'] DELETANDO FORM
			return render(request, 'apostas.html', {'form': form, 'partida': p})
		# else:
		# 	p = None #P = NADA
		# 	form = ApostaForm()
		# 	# form.fields['valor'].widget = HiddenInput()  ESCONDER O CAMPO
		# 	return render(request, 'apostas.html', {'form': form, 'partida': p})

def home(request):
	return render(request, 'home.html')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/bolao/login')
		return HttpResponse("Erro 404")
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'reg_form.html', args)

@login_required
def listajogos(request):
	partidas = Partida.objects.all()
	args = {'partidas': partidas}
	return render(request, 'listajogos.html', args)

@login_required
def times(request):
	times = selecao.objects.all()
	args = {'times': times}
	return render(request, 'times.html', args)


def view_perfil(request):
	return render(request, 'perfil.html')

@login_required
def editar_perfil(request):
	if request.method == 'POST':
		form = EditarPerfilForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/bolao/perfil')
	else:
		form = EditarPerfilForm(instance=request.user)
		del form.fields['password']
		args = {'form': form}
		return render(request, 'editar_perfil.html', args)

@login_required
def mudar_senha(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/bolao/perfil')
		else:
			return redirect('/bolao/mudar-senha')
	else:
		form = PasswordChangeForm(user=request.user)

		args = {'form': form}
		return render(request, 'mudar_senha.html', args)

@login_required
def minhas_apostas(request):
	apostas = aposta.objects.all()
	args = {'apostas': apostas}
	return render(request, 'minhas_apostas.html', args)
