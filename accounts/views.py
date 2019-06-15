from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Bug
from features.models import Feature
from django.http import JsonResponse


def index(request):
    """Return the index.html file and statistics"""
    
    
    return render(request,  'index.html')
    

def Get_Data(request,**kwargs):
    labels = ['Bugs','Features']
    bugs = Bug.objects.all().count()
    features = Feature.objects.filter(paid=True).count()
    default = [bugs, features]
    labels2 = ['Unpaid','Paid']
    paid = Feature.objects.filter(paid=True).count()
    unpaid = Feature.objects.filter(paid=False).count()
    default2 = [unpaid, paid]
    data= {
        "labels": labels,
        "default" : default,
        "default2": default2,
        "labels2" : labels2
    }
    # paid and unpaid features
    
    # data2= {
    #     "labels": labels2,
    #     "default" : default2,
    # }
    return JsonResponse(data)
    
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out", extra_tags="alert-success")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!", extra_tags="alert-success")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Your username or password is incorrect!", extra_tags="alert-danger")
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered", extra_tags="alert-success")
            else:
                messages.error(request, "Unable to register your account at this time", extra_tags="alert-danger")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})

@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    bugs = Bug.objects.filter(author=request.user.id)
    features = Feature.objects.filter(author=request.user.id)
    context =  { 
        'bugs' : bugs, 
        'features' : features,
        'profile' : user,
    }
    
    return render(request, 'profile.html', context)