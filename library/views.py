from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'nav' : [
            ['/', 'Home'],
            ['/manager/', 'Manager']
        ]
    }
    return render(request, 'library/index.html', context)