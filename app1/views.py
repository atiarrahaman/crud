from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from .models import *
from  .forms import *
from django.contrib  import messages 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash



# Create your views here. 


def home (request):
    st=Student.objects.all()
    if request.method == 'POST':
        fm= StudentForm(request.POST)
        if fm.is_valid():
            messages.success (request,'Added  Successfull !!')
            fm.save()
            fm= StudentForm()


    else:
        fm=StudentForm()     
    
    contex= {'form':fm, 'std':st}   
    return render (request,'home.html',contex)

def Delete_data(request,id):
    dl=Student.objects.get(id=id)
    dl.delete()
    msz='Delete Successfull!!'
    
    return redirect('/',)


def Edit_data(request,id):
    
    if request.method == 'POST':
      ed=Student.objects.get(id=id)
      fm=EditForm(request.POST,instance=ed)

      if fm.is_valid():
            fm.save()
            fm=EditForm()
            
    
    else:
        ed=Student.objects.get(id=id)
        fm=EditForm(instance=ed)

    
    return render(request,'edit.html',{'form':fm})


def Singup_Form(request):
    if request.method == 'POST':
        fm=SingUp_form(request.POST)
        if fm.is_valid():
           messages.success(request,'Account Created !')
           fm.save()
           fm=SingUp_form()
    else:
        fm=SingUp_form()
    context={'form':fm}
    return render (request,'singup.html',context)
def Login_form(request):
 
    if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if  fm.is_valid():
            messages.success(request,'Login Success !!')
            uname=fm.cleaned_data['username']
            pas=fm.cleaned_data['password']
            user=authenticate(username=uname,password=pas)
            if user is not None:
                login(request,user)
                return redirect('/profile') 
    else: 
      fm=AuthenticationForm()      
     
    return render(request,'login.html',{'form':fm})

def Profile(request):
    if request.user.is_authenticated:
         return render(request,'profile.html',{'name':request.user})
    
    else:
        return redirect('/login')

def Log_out(request):
    logout(request)
    return redirect('/login')


def ChangePassword(request):
    if request.method == 'POST':
        fm=PasswordChangeForm(user= request.user ,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return redirect('profile')

    else:
         fm=PasswordChangeForm(user= request.user)      
    context={'form':fm}
            
    return render (request,'changepass.html',context)
# def applyform (request):
#     if request.method =='POST':
#         fm=BloodForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm=BloodForm()
#     context= {'form':fm}
#     return render(request,'applyform.html',context)