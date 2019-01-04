from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    '''

    if request.method == 'POST':
        print(request.META)
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if form.is_valid():
            if not request.session.get('user'):
                request.session['user'] = username
                request.session['password'] = password
                return HttpResponse('welcome!')
            else:
                return HttpResponse('please login!')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    '''
    return render(request, 'login.html')

def logout(request):
    return HttpResponse('byebye!')