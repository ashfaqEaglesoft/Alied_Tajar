
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="home"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    path('addbusiness',views.add_business,name="addbusiness"),
    path('showbusiness',views.show_business,name="showbusiness"),
    path('updatebusiness/<int:id>',views.update_business,name="updatebusiness"),
]
