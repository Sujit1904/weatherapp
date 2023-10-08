from django.shortcuts import render
import requests
import datetime

def home(request):
    custom_error_message = None  # Initialize a custom error message as None

    if request.method == 'POST':
        city = request.POST['city']
    else:
        city = 'solapur'
    
    url = f"https://api.weatherapi.com/v1/current.json?key=c5e6022efbdc472583b143642232509&q={city}"
    
    try:
        r = requests.get(url)
        dict_w = r.json()
        
        if 'error' in dict_w:
            # Handle API error here if needed
            custom_error_message = "Please enter a correct city name"
        else:
            dict_weather = dict_w["current"]["temp_c"]
            description = dict_w['current']["condition"]["text"]
            icon = dict_w['current']["condition"]["icon"]
            
            return render(request, 'index1.html', {'city': city, 'temp': dict_weather, 'description': description, "icon": icon, 'custom_error_message': custom_error_message})
    
    except requests.exceptions.RequestException as e:
        # Handle request error here if needed
        custom_error_message = f"Request failed: {e}"
    except ValueError as e:
        # Handle JSON parsing error here if needed
        custom_error_message = f"JSON parsing error: {e}"

    return render(request, 'index1.html', {'custom_error_message': custom_error_message})
