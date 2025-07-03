from django.shortcuts import render, redirect
from django.contrib import messages
import os

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'credentials.txt')
        with open(file_path, 'r') as file:
            for line in file:
                user, pwd = line.strip().split(',')
                if user == username and pwd == password:
                    return redirect('welcome')
        messages.error(request, 'Sorry, only Ketaki can enter my heart 💖😁')
    return render(request, 'login.html')

def welcome(request):
    return render(request, 'welcome.html')

def love_letter(request, letter):
    messages_dict = {
        'K': 'Ketaki, you are the Key to my heart.',
        'E': 'Every moment with you is heaven.',
        'T': 'To love you is my destiny.',
        'A': 'All I want is your smile forever.',
        'K2': 'Kindness in your heart is my treasure.',
        'I': 'I love you more than the stars love the sky.',
    }
    message = messages_dict.get(letter.upper(), 'You are my everything.')
    return render(request, 'letter.html', {'letter': letter.upper(), 'message': message})


from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')  # or use named URL: redirect('login')
