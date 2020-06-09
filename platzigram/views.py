from django.http import HttpResponse

from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Datetime is {}'.format(now))

def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), content_type='application/json'
    )

def say_hi(request, name, age):
    # import pdb; pdb.set_trace()
    return HttpResponse('Hi {} you have {} years old'.format(name, age))
