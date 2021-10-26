from django.shortcuts import render
from decouple import config
import requests

def index(request):

    headers = {
            'X-AUTH-USER': config('KIMAI_X-AUTH-USER'),
            'X-AUTH-TOKEN': config('KIMAI_X-AUTH-TOKEN')
            }
    r = requests.get('http://' + config('KIMAI_HOST') + '/api/timesheets/active', headers=headers)
    r.raise_for_status()

    return render(request, "display/index.html", {"records": r.json()})
