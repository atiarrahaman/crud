from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>',views.Delete_data,name='delete'),
    path('edit/<int:id>',views.Edit_data,name='edit'),
    path('singup',views.Singup_Form,name='singup'),
    path('login',views.Login_form,name='login'),
    path('profile',views.Profile,name='profile'),
    path('logout',views.Log_out,name='logout'),
    path('changepass',views.ChangePassword,name='changepass'),
    # path('apply-form',views.applyform,name='apply-form'),
]
