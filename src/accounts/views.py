from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('/')
    else:
        signup_form = UserCreationForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/signup_form.html', context)
