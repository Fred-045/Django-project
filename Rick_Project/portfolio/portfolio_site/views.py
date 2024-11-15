from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    return render(request, 'portfolio_site/home.html')

def about(request):
    return render(request, 'portfolio_site/about.html')

def projects(request):
    return render(request, 'portfolio_site/projects.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact form data to the database
            return redirect('success')  # Redirect to success page
    else:
        form = ContactForm()

    return render(request, 'portfolio_site/contact.html', {'form': form})

def success(request):
    return render(request, 'portfolio_site/success.html')
