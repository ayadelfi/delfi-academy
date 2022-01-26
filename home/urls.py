
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('',views.home ,name="home"),
    path('register',views.register ,name="register"),
    path('login/',views.login ,name="login"),
    path('logout',views.logout ,name="logout"),
    path('niveaucours/<id>/',views.niveaucours,name="niveaucours"),
    path('coursdetails/<id>',views.CoursDetails,name="coursdetails"),
    path('cart',views.Cart, name="cart"),
    path('update_item/',views.UpdateItem, name="update_item"),
    path('profcours/<id>/',views.profcours),
    path('checkout/',views.Checkout, name="checkout"),
    path('mescours/',views.MesCours, name="mescours"),
    path('about',views.aboutus,name="about"),
    path('contact',views.contact,name="contact"),
    path('profs',views.profs,name="profs"),
    

    





]