from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Burada mesajı işleyebilirsin (örneğin e-posta ile gönderim ya da veri tabanına kayıt)
        # Şu anda sadece başarı mesajı dönecek:
        return HttpResponse(f"Thank you {name}, your message has been received!")
    
    return render(request, 'core/contact.html')

from django.shortcuts import render

def apply(request):
    return render(request, 'core/apply.html')