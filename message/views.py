from django.shortcuts import render

# Create your views here.
from message.forms import MessageForm
from message.models import Message


def my_message(request):
    form = MessageForm()
    message_list = Message.objects.all().order_by('-created_time')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    form = MessageForm()
    return render(request, 'message/my_message.html',locals())