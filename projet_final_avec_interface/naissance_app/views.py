from django.shortcuts import render, redirect
from .models import Utilisateur, nouveau_ne
from django.http import  HttpResponseRedirect, HttpResponse
from .forms import UtlisateurForm, nouveau_neForm
from django.db.models import fields, Q


# Create your views here.
def home(request):
	return render(request, 'enfant/home.html', {})

	

def nouveauNe_list(request):
	Nouveau_ne = nouveau_ne.objects.all().order_by('nom')
	return render(request, 'enfant/nouveauNe_list.html', {
		'Nouveau_ne': Nouveau_ne,
	})


def ajout_newborn(request):
	submitted = False
	#form=nouveau_neForm
	if request.method == "POST":
		form = nouveau_neForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ajout_newborn?submitted=True')
	else:
		form = nouveau_neForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request, 'enfant/ajout_newborn.html', {
		'form': form,
		'submitted': submitted,
	})


def update_newborn(request, nouveau_ne_id):
			Nouveau_ne = nouveau_ne.objects.get(pk=nouveau_ne_id)
			form = nouveau_neForm(request.POST or None, instance=Nouveau_ne)
			if form.is_valid():
				form.save()
				return redirect('nouveauNe_list')
			return render(request, 'enfant/update_newborn.html', {
				'Nouveau_ne': Nouveau_ne,
				'form': form,
			}) 


def delete_newborn(request, nouveau_ne_id):
					Nouveau_ne = nouveau_ne.objects.get(pk=nouveau_ne_id)
					Nouveau_ne.delete()
					return redirect('nouveauNe_list')


def show_newborn(request, nouveau_ne_id):
	Nouveau_ne = nouveau_ne.objects.get(pk=nouveau_ne_id)
	return render(request, 'enfant/show_newborn.html', {
		'Nouveau_ne': Nouveau_ne,
	})

def search_newborn(request):
	if request.method == "GET":
		query = request.GET.get('query')
		if query:
			mutiple_q = Q(Q(nom__icontains=query) | Q(prenom__icontains=query))
		Nouveau_ne = nouveau_ne.objects.filter(mutiple_q)
		if Nouveau_ne:
			return render(request, 'enfant/search_newborn.html', {
				'Nouveau_ne': Nouveau_ne
			})
		else:
			print('Not found ...')
			return render(request, 'enfant/not_found.html', {})


def user_list(request):
	utilisateur = Utilisateur.objects.all().order_by('nom')
	return render(request, 'enfant/user_list.html', {
		'utilisateur': utilisateur,
	})


def add_user(request):
	submitted = False
	#form=nouveau_neForm
	if request.method == "POST":
		form = UtlisateurForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_user?submitted=True')
	else:
		form = UtlisateurForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request, 'enfant/add_user.html', {
		'form': form,
		'submitted': submitted,
	})


def update_user(request, Utilisateur_id):
			utilisateur = Utilisateur.objects.get(pk=Utilisateur_id)
			form = UtlisateurForm(request.POST or None, instance=utilisateur)
			if form.is_valid():
				form.save()
				return redirect('user_list')
			return render(request, 'enfant/update_user.html', {
				'utilisateur': utilisateur,
				'form': form,
			}) 


def delete_user(request, Utilisateur_id):
					utilisateur = Utilisateur.objects.get(pk=Utilisateur_id)
					utilisateur.delete()
					return redirect('user_list')