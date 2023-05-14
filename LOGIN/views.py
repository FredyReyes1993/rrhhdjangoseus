from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from RRHHSEUSPROJECT import settings
from django.utils.encoding import force_bytes,force_str
from django.http import HttpResponse
from . tokens import generate_token
import sweetify


# Create your views here.
def home(request):

    return render(request, 'LOGIN/index.html')




def signup(request):

    if request.method == 'POST':
        mensaje= None
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        username = email.split('@')[0]

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone_number = phone
        myuser.save()

        mensaje = 'Usuario creado con éxito'

# Bienvenida por medio de correo
        subject = "Inicio de sessión RRHH|SEUS!"
        message = "Hello " + myuser.first_name + "!! \n" + \
            "Bienvenidos al Sistema Web RRHH!! \n\n. Te hemos enviado un correo , por favor confirma la dirección de tu correo ingresado. \n\nGracias\n RRHH"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

# Configuracion de correo electronico

        current_site = get_current_site(request)
        email_subject = 'Confirma tu correo electronico'
        message2 = render_to_string('email_confirmation.html', {

            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)

        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        

        return render(request, 'LOGIN/index.html', {'mensaje':mensaje})


    return render(request, 'LOGIN/signup.html')



#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
#@login_required(login_url="index")
def masterpage(request):
    if request.method == 'POST':
        mensajeMaster = None
        username = request.POST['username']
        pass1 = request.POST['pass1']
 
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            
            return render(request, 'LOGIN/masterpage.html')
        
        else:
            mensajeMaster = 'Usuario o contraseña incorrectas'
            return render(request, 'LOGIN/index.html', {'mensajeMaster':mensajeMaster})

    return render(request, 'LOGIN/masterpage.html')




def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)

        return redirect('home')
    else:
        return render(request, 'activation_failed.html')

def signout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión!!")
    return render(request, 'LOGIN/index.html')