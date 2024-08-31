from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, CustomerSignUpForm, ServiceSignUpForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'admin_register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_service:
                login(request, user)
                return redirect('service')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


@login_required
def admin(request):
    if request.user.is_authenticated and request.user.is_admin:
        return render(request, 'admin_dashboard.html')
    else:
        return render(request, 'login.html')


@login_required
def customer(request):
    if request.user.is_authenticated and request.user.is_customer:
        return render(request, 'customer_dashboard.html')
    else:
        return render(request, 'login.html')


@login_required
def service(request):
    if request.user.is_authenticated and request.user.is_service:
        return render(request, 'service_dashboard.html')
    else:
        return render(request, 'login.html')

def customer_register(request):
    msg = None
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = CustomerSignUpForm()
    return render(request, 'customer_register.html', {'form': form, 'msg': msg})


def service_register(request):
    msg = None
    if request.method == 'POST':
        form = ServiceSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = ServiceSignUpForm()
    return render(request, 'service_register.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    # Optionally redirect to a specific page after logout
    return redirect('login_view')  # Redirect to login page (replace with desired URL)
