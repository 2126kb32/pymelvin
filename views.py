from django.shortcuts import render,redirect
from .forms import HomeForm
from .forms import LoginForm
from .models import UserProfile

  
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # For simplicity, the password is stored in plain text. In a real application, use a secure method.
            user = UserProfile.objects.filter(username=username, password=password).first()

            if user:
                # Perform the login action, for example, set a session variable.
                # In a real application, consider using Django's built-in authentication system.
                request.session['username'] = username
                return redirect('success')  # Redirect to a success page
    else:
        form = LoginForm()

    return render(request, 'login.html')
def home_view(request):
    form = HomeForm()  # Create an instance of your form
    return render(request, 'home.html', {'form': form})
