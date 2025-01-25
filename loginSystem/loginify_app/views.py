from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import UserDetailForm
from .models import UserDetail

# Create your views here.
def home(request):
    return render(request, "loginify_app/home.html", {'page_name':'Home'})

def login(request):
    if request.method == "POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user = UserDetail.objects.get(email=email)
        if user.password == password:
            request.session["email"] = email
            return redirect('loginify_app:profile')
        else:
            return render(request, "loginify_app/login.html", {'page_name':'Login','error': True, 'success': False, 'message': 'Invalid details!'})
    else:
        return render(request, "loginify_app/login.html", {'page_name':'Login'})

def signup(request):
    if request.method == "POST":
        user_detail_form = UserDetailForm(request.POST)
        if user_detail_form.is_valid():
            user_detail_form.save()
            return render(request, "loginify_app/signup.html", {'page_name':'Signup','form':user_detail_form, 'error': False, 'success': True, 'message': 'Successfully added!'})
        else:
            return render(request, "loginify_app/signup.html", {'page_name':'Signup','form':user_detail_form, 'error': True, 'success': False, 'message': 'Somthing wrong!'})
    else:
        user_detail_form = UserDetailForm()
        return render(request, "loginify_app/signup.html", {'page_name':'Signup','form':user_detail_form, 'error': False, 'message': ''})
    
def profile(request):
    email = request.session.get('email')
    user = UserDetail.objects.get(email=email)
    return render(request, "loginify_app/profile.html", {'page_name':'My Profile','user':user})

def logout(request):
    del request.session['email']
    return redirect('loginify_app:login')