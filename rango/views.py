from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    #'/rango/about/'
    context_dict={'boldmessage': 'This tutorial has been put together by 2403203P'}
    return render(request, 'rango/about.html', context=context_dict)

def index(request):
    # Construct a dictionary to pass to the template engine as its context. 
    # Note the key MUST match to {{ key }} in the template! 
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    
    # Return a rendered response to send to the client. 
    # We make use of the shortcut function. 
    # Note that the first parameter is the template we wish to use. 
    return render(request, 'rango/index.html', context=context_dict)
