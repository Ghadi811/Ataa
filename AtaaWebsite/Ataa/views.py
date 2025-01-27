from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, EmailLoginForm
from django.db import transaction
from .models import Doneer, Donee, items

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_type = form.cleaned_data['user_type']
            user.username = email
            user.set_password(password)

            try:
                with transaction.atomic():
                    user.save()
                    if user_type == 'doneer':
                        Doneer.objects.create(
                            firstname=first_name,
                            lastname=last_name,
                            email=email,
                            password=user.password
                        )
                    elif user_type == 'donee':
                        Donee.objects.create(
                            firstname=first_name,
                            lastname=last_name,
                            email=email,
                            password=user.password
                        )
                    user = authenticate(username=email, password=password)
                    auth_login(request, user)
                    return redirect('profile')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = EmailLoginForm()
    return render(request, 'login.html', {'form': form})



def profile(request):
    user = request.user
    user_type = None
    user_data = None
    try:
        if Doneer.objects.filter(email=user.email).exists():
            user_type = 'Doneer'
            user_data = Doneer.objects.get(email=user.email)
        elif Donee.objects.filter(email=user.email).exists():
            user_type = 'Donee'
            user_data = Donee.objects.get(email=user.email)
    except Doneer.DoesNotExist:
        user_data = None
    except Donee.DoesNotExist:
        user_data = None

    if user_data:
        context = {
            'first_name': user_data.firstname,
            'last_name': user_data.lastname,
            'email': user_data.email,
            'user_type': user_type,
        }
    else:
        context = {
            'first_name': 'N/A',
            'last_name': 'N/A',
            'email': user.email,
            'user_type': 'Unknown',
        }

    return render(request, 'profile.html', context)


def logout_view(request):
    auth_logout(request)
    return redirect('home')

def items(request):
    all_items = items.objects.all().select_related('category').values()
    template = loader.get_template('Items.html')
    context = {
        'all_items': all_items,
    }
    return HttpResponse(template.render(context, request))
def homepage(request):
    return render(request, 'homepage.html')
