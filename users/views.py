from django.shortcuts import render

# Create your views here.
def know_me(request):

    return render(request,'users/show_jq.html')