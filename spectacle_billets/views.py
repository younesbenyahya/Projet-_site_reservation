from django.http import HttpResponse

# Cette fonction renvoie la page d'accueil du site / This function returns the home page of the site
def home(request): 
    return HttpResponse('Home_page')