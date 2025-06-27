from django.shortcuts import render

def index(request):
    context = {
        'name' : 'Home',
        'title' : 'Humans Storys',
        'range_list': range(1, 9),
        'nav' : [
            ['/library/', 'Library'],
            ['/manager/', 'Manager'],
            ['/blog/', 'blog']
        ]
    }
    return render(request, 'index.html', context)