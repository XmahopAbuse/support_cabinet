from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import  render
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import LoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'], # authenticate compare data with database, return User object if ok
                                password=cd['password'])


        if user is not None:
            if user.is_active:
                login(request,user) # saving user in session
                return HttpResponse("Успешная автризация")
            else:
                return HttpResponse("Пользователь неактивен")
        else:
            return HttpResponse("Неверный логин и/или пароль")
    else:
        form = LoginForm()

    return render(request,'account/login.html', {'form':form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return JsonResponse({'status':'Ok',
                                'message':'Пароль изменен'})
        else:
            return JsonResponse({'status':'Error',
                                'message':'Произошла ошибка, проверьте правильность данных и попробуйте снова'})
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}