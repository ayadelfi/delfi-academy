from django.contrib import auth

from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

import datetime

from django.template import context

from home.models import  Client, Formation, Niveau, Order, OrderItem, Prof, Video, année,Contact
import json

# Create your views here.

def home(request):
    formations = Formation.objects.all()
    profs=Prof.objects.all()
    if request.user.is_authenticated:
        customer = request.user.client
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
    
        num_item=order.get_cart_item
        

    else:
        items=[]
        num_item=0
        order = {'get_cart_total': 0 , 'get_cart_item':0}
    clients = Client.objects.all()    
    
   
    cpt = 0
    cpt2=0
    cpt3=0
    for client in clients:
        cpt2 = cpt2 + 1 
    for formation in formations : 
        cpt = cpt + 1
    for prof in profs:
        cpt3 = cpt3 + 1 
    niveaux = Niveau.objects.all()
    années = année.objects.all() 
    context={'formations':formations , 'num_item':num_item, 'profs':profs,'niveaux':niveaux,'années':années , 'cpt':cpt , 'cpt2':cpt2,'cpt3':cpt3 }
    return render(request,'home.html',context)

def niveaucours(request,id):
    année_id=id
    annéess = année.objects.get(id=année_id)
    formations = Formation.objects.filter(année = annéess)
    if request.user.is_authenticated:
        customer = request.user.client
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        num_item=order.get_cart_item

    else:
        num_item=0
        items=[]
        order = {'get_cart_total': 0 , 'get_cart_item':0}
    
    niveaux = Niveau.objects.all()
    années = année.objects.all()
    context={'formations':formations ,'num_item':num_item , 'annéess':annéess,'années':années,'niveaux':niveaux}
    return render(request,'3P.html',context) 

def register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

         

        if User.objects.filter(username=username):
            exist = True
            return render(request ,'register.html', {'exist':exist})
    
        else:
            exist = False
            user = User.objects.create_user( username=username, password=password1)
            client = Client.objects.create(user=user, name=username, phone=phone)
            user.save()
            client.save()
            user = auth.authenticate(username=username, password=password1)

            if user is not None:
                auth.login(request, user)
                return redirect("/")

      
    return render(request,'register.html')    

def login(request):
    if request.user.is_active:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
			
			
        else:
            exists = True
            return render(request ,'login.html', {'exists':exists})

    
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def CoursDetails(request,id):
    if request.user.is_authenticated:
        customer = request.user.client
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        num_item=order.get_cart_item

    else:
        num_item=0;
        items=[]
        order = {'get_cart_total': 0 , 'get_cart_item':0}
    formations = Formation.objects.all()
    formation_id=id
    formation = Formation.objects.get(id=formation_id)
    videos = Video.objects.filter(product=id)
    context={'formations':formations , 'formation':formation, 'videos':videos ,'num_item':num_item }
    return render(request,"coursdetails.html",context)

def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.client
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        num_item=order.get_cart_item
        total=sum([item.product.prix for item in items])


    else:
        items=[]
        order = {'get_cart_total': 0 , 'get_cart_item':0}
    niveaux = Niveau.objects.all()
    années = année.objects.all()    
    context={'items':items , 'order':order,'num_item':num_item,'total':total,'niveaux':niveaux,'années':années}    
    return render(request,"panier.html",context)

def UpdateItem(request):
    data = json.loads(request.body)
    productID= data['productID']
    action = data['action']
    print('action:', action)
    print('productID',productID)
    customer=request.user.client
    product=Formation.objects.get(id=productID)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)
    orderItem.save()
    if action == 'remove':
        orderItem.delete() 
    
    return JsonResponse('item was added',safe=False)    

def profcours(request,id):
    prof_id=id
    profs=Prof.objects.get(id=prof_id)
    formations=Formation.objects.filter(prof=profs)
    if request.user.is_authenticated:
        customer = request.user.client
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        num_item=order.get_cart_item

    else:
        num_item=0
        items=[]
        order = {'get_cart_total': 0 , 'get_cart_item':0}

    context={'formations':formations , 'profs':profs,'num_item':num_item,'itmes':items}
    return render(request,'profcours.html', context)

def Checkout(request):
        if request.user.is_authenticated:
            customer = request.user.client
            order,created=Order.objects.get_or_create(customer=customer,complete=False)
            items= order.orderitem_set.all()
            num_item=order.get_cart_item
            total=sum([item.product.prix for item in items])

            if request.method == 'POST':
                
                    if len(request.FILES) != 0:
                        reçu=request.FILES['reçu']
                        print('yes boulili')
                        order.total = total 
                        order.phone= customer.phone           
                        order.reçu= reçu
                        order.transaction_id=datetime.datetime.now()
                        order.complete= True
                        order.save()
                    return HttpResponseRedirect('/')       
                       
                     
                      
                
            else:    
                items=[]
                order = {'get_cart_total': 0 , 'get_cart_item':0}
        else:
            items=[]
            order = {'get_cart_total': 0 , 'get_cart_item':0}
        context={'items':items , 'order':order,'num_item':num_item,'total':total}        
        return render(request,"checkout.html", context)

  

def MesCours(request):
    if request.user.is_authenticated:
        customer = request.user.client
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        num_item=order.get_cart_item

    else:
        num_item=0
        items=[]
        order = {'get_cart_total': 0 , 'get_cart_item':0}
    if request.user.is_authenticated:
        customer = request.user.client
        
        orders = Order.objects.all()
        itemss=OrderItem.objects.all()
        videos=Video.objects.all()
       

    context={'orders':orders,'itemss':itemss ,'customer': customer,'videos':videos,'num_item':num_item,'items':items }
    return render(request,'mesCours.html',context) 



def aboutus(request):
    niveaux = Niveau.objects.all()
    années = année.objects.all()
    if request.user.is_authenticated:
        customer = request.user.client
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        num_item=order.get_cart_item

    else:
        num_item=0
        items=[]
        order = {'get_cart_total': 0 , 'get_cart_item':0}
    context={'niveaux':niveaux,'années':années,'num_item':num_item , 'items':items}
    return render(request,'aboutus.html',context)    

def contact(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('message'):
            contact= Contact()
            contact.nom = request.POST.get('name')
            contact.phone=request.POST.get('phone')
            contact.email=request.POST.get('email')
            contact.message=request.POST.get('message')
            contact.save()
            return render(request,'contact.html' ) 
            print('')
        else:
            return render(request,'contact.html' )

    if request.user.is_authenticated:
            customer = request.user.client
            order,created=Order.objects.get_or_create(customer=customer,complete=False)
            items= order.orderitem_set.all()
            num_item=order.get_cart_item

    else:
            num_item=0
            items=[]
            order = {'get_cart_total': 0 , 'get_cart_item':0}    
    niveaux = Niveau.objects.all()
    années = année.objects.all()
    
    context={'niveaux':niveaux,'années':années,'items':items,'num_item':num_item}
    return render(request,'contact.html' , context) 

def profs(request ):

    if request.user.is_authenticated:
        customer = request.user.client
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        num_item=order.get_cart_item

    else:
        num_item=0
        items=[]
        order = {'get_cart_total': 0 , 'get_cart_item':0}
    profs = Prof.objects.all()
    niveaux = Niveau.objects.all()
    années = année.objects.all()
    context={'niveaux':niveaux,'années':années,'profs':profs,'num_item':num_item,'items':items}
    return render(request,'profs.html',context)

