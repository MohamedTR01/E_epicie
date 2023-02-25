from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Client
from .models import Produit
from .forms import ClientForm
from .forms import ProduitForm

# Create your views here.

def home(request):
    return render(request,'home.html')
def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            # messages.success(request, 'Bienvenu')
            return redirect("profile")
        else:
            messages.error(request,"Erreur d'authentification")
            return redirect('login')
    return render(request, "login.html")    
    # return render(request, "login.html")
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if User.objects.filter(username=username):
            messages.error(request, "ce nom d'utilisateur a été déjà utilisé")
            return redirect('register')
        if User.objects.filter(email=email):
            messages.error(request, "cet email a déjà un compte")
            return redirect('register')
        if password != password1:
            messages.error(request, "les deux mots de passe ne correspondent pas")
            return redirect('register')
        if not username.isalnum():
            messages.error(request, "le nom d'utilisateur doit être alphanumeric")

        mon_utilsateur = User.objects.create_user(username,email,password)
        mon_utilsateur.first_name = firstname
        mon_utilsateur.last_name = lastname
        mon_utilsateur.save()
        messages.success(request, "Votre compte a été créé avec succès")
        return redirect('login')
    return render(request,'register.html')
def contacte(request):
    return render(request,'contacte.html')
def logout(request):
    logout(request)
    messages.success(request,'Vous etes déconnecté')
    return redirect('home')
# def client(request):
#     return render(request,'client.html')

def profile(request):
    user=request.user 
    return render(request,'compte.html',{'username':user})

def client(request):
    clients = Client.objects.all()
    context={"clients":clients}
    return render(request,'client.html',context)

def ajouter_client(request):
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    context={'form':form}
    return render(request,'ajouter_client.html',context)

def modifier_client(request,pk):
    client = Client.objects.get(id=pk)
    form=ClientForm(instance=client)
    if request.method=='POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('client')
    context={'form':form}
    return render(request,'ajouter_client.html',context)

def supprimer_client(request,pk):
    client = Client.objects.get(id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('client')
    context={'item':client}

    return render(request,'supprimer_client.html',context)


def produit(request):
    produits = Produit.objects.all()
    context={"produits":produits}
    return render(request,'produit.html',context)

def ajouter_produit(request):
    form=ProduitForm()
    if request.method=='POST':
        form=ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit')
    context={'form':form}
    return render(request,'ajouter_produit.html',context)

def modifier_produit(request,pk):
    produit = Produit.objects.get(id=pk)
    form=ProduitForm(instance=produit)
    if request.method=='POST':
        form=ProduitForm(request.POST,instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit')
    context={'form':form}
    return render(request,'ajouter_produit.html',context)

def supprimer_produit(request,pk):
    produit = Produit.objects.get(id=pk)
    if request.method=='POST':
        produit.delete()
        return redirect('produit')
    context={'item':produit}

    return render(request,'supprimer_produit.html',context)


def a_propos(request):
    return render(request,'a_propos.html')

