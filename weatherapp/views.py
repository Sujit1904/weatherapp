# from django.shortcuts import render
# import requests
# import datetime

# # Create your views here.
# def home(request):
#     if 'city' in request.POST:
#         city = request.POST['city']
#     else:
#         city ='solapur'

#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5894e6e8e2afced9562bad1351aeeb17'
#     PARAMS ={'units':'metric'}
#     data = requests.get(url,params=PARAMS).json()
#     description = data['weather'][0]['description']
#     icon = data['weather'][0]['icon']
#     temp = data['main']['temp']
#     day = datetime.date.today()

#     return render(request,'index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city })












import json
from django.shortcuts import render
from django.contrib import messages
import requests
import urllib.request
import datetime


def home(request):
          if request.method =='POST':
                  city = request.POST['city']
          else:
                  city = 'solapur'
          url = f"https://api.weatherapi.com/v1/current.json?key=c5e6022efbdc472583b143642232509&q={city}"
          try:
               r = requests.get(url)
               dict_w = json.loads(r.text)
               dict_weather = dict_w["current"]["temp_c"]
               description = dict_w['current']["condition"]["text"]
               icon = dict_w['current']["condition"]["icon"]
               
               print(dict_weather, description)
               return render(request,'index1.html' ,{'city':city,'temp':dict_weather,'description':description,"icon":icon,} )
          except requests.exceptions.RequestException as e:
                 exception_occurred = True
                 messages.error(request, f'Error: {e}')
                 return render(request, 'index1.html', {'city': city, 'exception_occurred': exception_occurred})
          except KeyError:
               exception_occurred = True
               messages.error(request, 'Entered data is not available from the API')
               return render(request, 'index1.html', {'city': city, 'exception_occurred': exception_occurred})
         
               