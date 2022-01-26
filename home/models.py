from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.files import FileField, ImageField
from django.conf import settings

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Niveau(models.Model):
    nom=models.CharField(max_length=255 , blank=False,null=False )
    def __str__(self):
        return self.nom

class année(models.Model):
    niveau=models.ForeignKey(Niveau, default=None, on_delete=models.CASCADE)
    nom=models.CharField(max_length=255 , blank=False,null=False )
    def __str__(self):
        return self.nom

class Prof(models.Model):
    image = models.ImageField()
    nom = models.CharField(max_length=255 , blank=True,null=True)
    matière = models.CharField(max_length=255 , blank=True,null=True , default="")
    def __str__(self):
        return self.nom
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url='images/no-image.png'
        return url

    @property
    def nbr_formation(self):
        nbr = self.formation_set.all()
        cptt = 0
        for n in nbr : 
            cptt = cptt + 1
        return cptt 
    
class Formation(models.Model):
    année=models.ForeignKey(année, default=None, on_delete=models.CASCADE)
    nom=models.CharField(max_length=255 , blank=False,null=False )
    description=models.TextField()
    prix = models.IntegerField(blank=False,null=False)
    prof = models.ForeignKey(Prof,on_delete=models.CASCADE , blank=False, null=False)
    nombre_cours = models.CharField(max_length=255,blank=True,null=False)
    durée_formation = models.CharField(max_length=255,blank=True,null=False)
    image = models.ImageField()
    série=models.FileField(upload_to ='uploads/')

    @property
    def sérieURL(self):
        try:
            url=self.série.url
        except:
            url='images/no-image.png'
        return url

    @property
    def get_nb_achat(self):
        orderitems=self.orderitem_set.all()
        total = 0
        for item in orderitems:
            if self is None:
                total = 0
            if item.order.active == True:
                total = total + 1
        return total        
    
    def __str__(self):
        return self.nom
    

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url='images/no-image.png'
        return url


class Video(models.Model):
    titre=models.CharField(max_length=255 , blank=False ,null=False)
    product=models.ForeignKey(Formation, default=None, on_delete=models.CASCADE)
    video = models.FileField()
   
    def __str__(self):
        return self.titre

    @property
    def videoURL(self):
        try:
            url=self.video.url
        except:
            url='images/no-image.png'
        return url    


class Order(models.Model):
    customer = models.ForeignKey(Client ,on_delete=models.SET_NULL , blank=True, null=True )
    phone = models.CharField(max_length=200 , null=True)
    date_ordred = models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False , null=True,blank=False)
    transaction_id = models.CharField(max_length=200 , null=True)
    total=models.FloatField(default=0.0)
    reçu = models.ImageField(upload_to='images',blank=True,null=True)
    active=models.BooleanField(default=False , null=True,blank=False)
 
    def __str__(self):
        return str(self.id) + ' -- ' + str(self.complete)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.product.prix for item in orderitems])
        return total 

    @property
    def get_cart_item(self):
        orderitems=self.orderitem_set.all()
        cpt = 0
        for item in orderitems:
            cpt= cpt + 1
        return cpt    
    

class OrderItem(models.Model):
    product=models.ForeignKey(Formation,on_delete=models.SET_NULL , blank=True, null=True )    
    order=models.ForeignKey(Order,on_delete=models.SET_NULL , blank=True, null=True)
    quntity = models.IntegerField(default=0, null=True , blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.nom)



class Contact(models.Model):
    nom = models.CharField(max_length=255, blank=True , null=True)
    email = models.EmailField(max_length=255,null=True,blank=True) 
    phone = models.CharField(max_length=255, null=True , blank=True)  
    message = models.TextField()     

    def __str__(self):
        return self.nom
