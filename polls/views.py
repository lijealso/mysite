from django.http import HttpResponse


def index(request):
    return HttpResponse("""Hello, world. You're at the polls index.
    </br>Olá. Esta é a página principal dos questionários...""")
