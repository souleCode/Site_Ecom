from django.shortcuts import render,redirect
from. models import Product,Commande
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    product_obj = Product.objects.all()
    item_name =request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_obj = Product.objects.filter(title__icontains=item_name)
    #--------------------------------pagination-----------------------------
    paginator = Paginator(product_obj,4) 
    page = request.GET.get('page')
    product_obj = paginator.get_page(page) 
    return render(request, 'shope/index.html',{'product_obj': product_obj})



def detail(request,myId):
    product_obj =Product.objects.get(id=myId)
    return render(request, 'shope/detail.html',{'product_obj':product_obj})


def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        total =request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipecode = request.POST.get('zipecode')
        comm = Commande(nom=nom,total=total, address=address,email=email,ville=ville,pays=pays,zipecode=zipecode,items=items)
        comm.save()
        return redirect('confirmation')
    return render(request, 'shope/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1] #pour couper le premier element en tete on utilise [:1] sanchant bien que les element son classes par(-date_commande)
    for item in info:
        nom = item.nom
    context ={
        'nom':nom,
    }    
    return render(request, 'shope/confirmation.html',context)