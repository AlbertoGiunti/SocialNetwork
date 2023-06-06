from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth  # auth serve per autenticare l'utente
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    # Se il metodo della richiesta è POST, allora l'utente ha inviato i dati del form
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # controllo se l'username o l'email sono già presenti nel db
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('signup')
            else:
                # creo l'utente
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log in automatico dopo la registrazione e reindirizzo al profilo

                # Crea un Profilo per l'utente appena registrato
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def login(request):
    # Se il metodo della richiesta è POST, allora l'utente ha inviato i dati del form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # controllo se l'username o l'email sono già presenti nel db
        if User.objects.filter(username=username).exists():
            # log in automatico dopo la registrazione e reindirizzo al profilo
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('profile')
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')

    else:
        return render(request, 'login.html')
