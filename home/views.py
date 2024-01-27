from django.shortcuts import render

# Create your views here

def index(request):
    """ View that returns the index page """
    
    return render(request, 'home/index.html')

def custom_404_view(request, exception):
    ''' render 404 page '''
    return render(request, '404.html', status=404)