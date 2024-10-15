from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render 

from .forms import SignUpForm
# Create your views here.
def index(request):
    return render(request, "core/index.html")

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})

def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("index")
    
    return render(request, "core/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")