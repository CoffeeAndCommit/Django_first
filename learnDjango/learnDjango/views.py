

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
 

def home(request):
    # return HttpResponse("Hello world . You are here in django world")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Example: send an email (configure EMAIL_BACKEND in settings)
        # send_mail(
        #     f"Message from {name}",
        #     message,
        #     email,
        #     ['youremail@example.com'],
        # )

        # Or you can just pass a “thanks” flag to template
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')