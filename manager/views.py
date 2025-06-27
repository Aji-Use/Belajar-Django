from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'nav' : [
            ['/', 'Home'],
            ['/library/', 'Library']
        ]
    }
    return render(request,'manager/index.html', context)