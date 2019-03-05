from django.http import HttpResponse

def light(request):
    return HttpResponse('This is the light/ endpoint!')
