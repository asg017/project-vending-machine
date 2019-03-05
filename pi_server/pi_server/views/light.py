from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from gpiozero import LED

SECRET = 'SECRET SECRET'
LIGHT_PIN = 17

@csrf_exempt
def light(request):

    if request.method != 'POST':
        return HttpResponseBadRequest('You must make a post request!')

    data = json.loads(request.body.decode('utf-8'))

    if data.get('secret') != SECRET:
        return HttpResponseForbidden('Secrets dont match!')

    led = LED(LIGHT_PIN)
    led.blink()

    return HttpResponse('Blinked the LED!')
