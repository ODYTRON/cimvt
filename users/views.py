from django.shortcuts import render, redirect
# this is to create user forms
# from django.contrib.auth.forms import UserCreationForm (replaced)
# this is to have flash messages for checking the form data
from django.contrib import messages
# you made a forms.py form to inherit all the attributes of UserCreAtionForm (you made a function there UserRegisterForm)
# so you have to replace usercration with user register
# here you import the forms
from .forms import UserRegisterForm,  UserUpdateForm, ProfileUpdateForm
# with this decorator you make the session for every user you need to login to be in your own space
from django.contrib.auth.decorators import login_required



# Create your views here.

def register(request):
    if request.method == 'POST':
        # if there is a request with post make an isntance of the form with the posted data
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # flash message
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        # create a new blank instance of the form
        form = UserRegisterForm()
        # return this instance in the template register.html
    return render(request, 'users/register.html', {'form': form})



# add the decoratror for session adds functionallity to existing function in our case our user must login to see this view
@login_required
def profile(request):
    if request.method == 'POST':
        # instanciate forms
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # flash message
            messages.success(request, f'your profile has been updated')
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    # pass the forms to the template
    context = {
            'u_form': u_form,
            'p_form': p_form
        }
        # add every form in return to access it
    return render(request, 'users/profile.html', context)






