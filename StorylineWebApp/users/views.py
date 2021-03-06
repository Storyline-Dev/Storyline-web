from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ClientRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def clinicianHome(request):
    return render(request, 'users/clinicianHome.html')

@login_required
def registerClient(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'You have successfully added a new client.')
            return redirect('clinician-home')
    else:
        form = ClientRegisterForm()

    return render(request, 'users/registerClient.html', {'form': form})

@login_required
def clientHome(request):
    return render(request, 'users/clientHome.html')

@login_required
def clinicianProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(
                request, f'Your account has been updated!')
            return redirect('clinician-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/clinicianProfile.html', context)

@login_required
def clientProfile(request):
    return render(request, 'users/clientProfile.html')
