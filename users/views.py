from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import Group
from django.contrib import messages
#___________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________
from .models import Profile


#___________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________


def profile(request ):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user_id=request.user.id).first()

        context = {
            'profile' : profile,
        }
        return render(request, 'profile.html', context=context)
    else: 
        return redirect('/signin')

def dashboard(request):
    return render(request, 'dashboard.html')


#______________________________________________________________________________________________________________________________________________________________________
# user view custom
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='all_Users')
            user.groups.add(group) 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            userNow = authenticate(username=username, password=password)
            login(request, userNow)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('/signin')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('password_change')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'registration/password_change_form.html', {
            'form': form
        })
    else:
        messages.error(request, 'you are unable to perfor this action beacause you are not signed in')
        return redirect('/signin')