from django.http import HttpResponse

def index(request):
    """
    Index page for the site 
    """
    return HttpResponse("Hello, Python Class.")
    #return render(request, 'tracks/index.html')
