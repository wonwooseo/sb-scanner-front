from django.shortcuts import render
from datetime import *
import requests


api_url = "https://api.sb-scanner.info/latest"


# Create your views here.
def index(request):
    resp = requests.get(api_url).json()
    for item in resp:
        parsed_time = datetime.strptime(item["date"], '%Y-%m-%dT%H:%M:%S%z')
        item["date"] = parsed_time.strftime('%Y/%m/%d %H:%M')
        # TODO: missing avatar urls?
    return render(request, "index.html", {"commit_list": resp})
