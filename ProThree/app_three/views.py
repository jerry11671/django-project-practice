from django.shortcuts import render
# from django.http import HttpResponse
# from .models import User
from app_three.forms import UserForm

def index(request):
    return render(request, 'app_three/index.html')

# def user(request):
#     user_data = User.objects.order_by('first_name')
#     userdict = {'user_list': user_data}
#     return render(request, 'app_three/help.html', context=userdict)

def Users(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request, 'app_three/users.html', context={'form': form})
