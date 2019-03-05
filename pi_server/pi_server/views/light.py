from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from gpiozero import LED

SECRET = ''
LIGHT_PIN = -1

@csrf_exempt
def light(request):

    if request.method != 'POST':
        return HttpResponseBadRequest('You must make a post request!')

    data = json.loads(request.body.decode('utf-8'))

    # TODO
    # 1. Check if the secret inside of "data" matches the SECRET above!
    #       If no, return a HttpResponseForbidden
    # 2. Blink the LED!

    return HttpResponse('Change this message!')
