from django.shortcuts import render,redirect
from .form import AdministratorForm
from django.http import JsonResponse
from .models import Administrator

# Create your views here.
def add_user(request):
    form = AdministratorForm()
    context = {
        'form':form,
        'success' : 'Data berhasil ditambahkan'
    }  
    if request.method == 'POST':
        data = AdministratorForm(request.POST)
        
        if data.is_valid(): 
            data.save()
            return redirect('users:administrator')
        else:
            return JsonResponse({'message':data.errors}, status=400)
    return render(request, 'users/add_user1.html', context)


def read_data(request):
    data = Administrator.objects.all() # pylint: disable=no-member
    context = {
        'data_users':data
    }
    return render(request, 'users/administrator.html', context)
    
# def administrator(request):
    
#     return render(request, 'administrator/administrator.html')