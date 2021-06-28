from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import action, api_view
from financial_chat.generics import *

from main.models import *
from .serializers import *
from .forms import *

import csv


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, labels('success.succesful_registration'))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def index(request):
    template_name = 'index.html'
    chat, created = Chat.objects.get_or_create(title='Main Chat')
    context = {'chat': chat.id}
    return render(request, template_name, context)

#################
# Message
#################

@api_view(('GET',))
@login_required
def messageList(request):
    relationship = validateRelationship(request)
    if relationship:
        return relationship

    data = request.GET
    serializer = MessageSerializerList(Message.objects.filter(chat=data.get('chat')), many=True)
    return JsonResponse(serializer.data[:50], safe=False)

@api_view(('POST',))
@login_required
def messageCreate(request):
    relationship = validateRelationship(request)
    if relationship:
        return relationship

    data = request.POST
    _mutable = data._mutable
    data._mutable = True
    data['user'] = User.objects.get(username=request.user).id
    data._mutable = _mutable

    if data.get('content')[0] == '/':
        return invokeCommand(request)
    serializer = MessageSerializerCreate(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'detail': labels('success.success'), 'error': 0})
    else:
        return JsonResponse(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(('POST',))
def messageCreateBOT(request):
    relationship = validateRelationship(request)
    if relationship:
        return relationship

    data = request.POST.copy()
    serializer = MessageSerializerCreate(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'detail': labels('success.success'), 'error': 0})
    else:
        return JsonResponse(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

def invokeCommand(request):
    data = request.POST.copy()
    contentSplit = data.get('content').split('=')
    if len(contentSplit) > 1:
        command = contentSplit[0].strip()
        if command == '/stock':
            data['stock_code'] = contentSplit[1].strip()
            return stock(request, data)
        elif command == '': # For future commands
            pass

    return JsonResponse({'detail': labels('error.command_error'), 'error': 1})

def stock(request, data):
    return requestApi(request, 'stock/', method='POST', data=data)
