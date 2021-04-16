from django.shortcuts import render
from django.http import HttpResponse
import requests
import random
# Create your views here.

def index(request):
    if request.method == "POST":
        city = request.POST.get('search_loc')
        
    else:
        random_cities = ["Hong Kong", "Bangkok", "London","Singapore","Macau","Paris","Dubai","Kuala Lumpur","Istanbul","Rome","Delhi","Mumbai","California"]
        city=random.choice(random_cities)


    api='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=76820f87246d426cfef2c751d89cecb5'
    api_json = requests.get(api.format(city)).json()
    result = {
        'city':city,
        'weather': api_json['main']['temp'],
        'desc': api_json['weather'][0]['main'],
        'icon': api_json['weather'][0]['icon'],
    }
    if result['weather'] >10:
        a=1
    else:
        a=2
    
    
    print(api_json)
    context = {'result':result,'a':a}
    return render(request,'home.html', context)