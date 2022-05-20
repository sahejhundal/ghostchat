from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Message

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def login(request):
    print (request.POST)
    print("yo fuckyy")
    if request.method=='POST':
        username = request.POST.get('username')
        if username:
            response = HttpResponse("<a href='/'>Success! Click here to chat!</a>")
            response.set_cookie('user', username)
            return response
    else:
        return render(request, 'loginpage.html')

def chat(request):
    user=request.COOKIES.get('user')
    if not user:
        return login(request)
        username = request.POST.get('username')
        if username:
            response = HttpResponse("<a href='/'>Success! Click here to chat!</a>")
            response.set_cookie('user', username)
            return response
    if request.method=='POST':
        m = request.POST.get('message')
        client_ip=get_client_ip(request)
        client_ip=client_ip.replace(".", "")
        message = Message(username=user,userip=client_ip,content=m,senttime=timezone.now(),
        color="#" + client_ip[:6])
        message.save()
        return index(request)

def index(request):
    """View function for home page of site."""
    #client_ip=get_client_ip(request)
    #client_ip=client_ip.replace(".", "")
    #print(client_ip)
    user=request.COOKIES.get('user')
    if not user:
        return login(request)

    # Generate counts of some of the main objects
    messagescount = Message.objects.all().count()
    messages = Message.objects.all()

    context = {
        'messages': messages,
        'messagescount': messagescount,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class MessagesView(generic.ListView):
    model = Message
