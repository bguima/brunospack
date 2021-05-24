import requests
import urllib.parse

def weather_forecast():
    # TODO: Return a 5-element list of weather forecast for a given woeid

    url = "https://www.metaweather.com/api/location/"
    woeid = '638242' #str(woeid)
    response = requests.get(url+woeid).json()
    
    forecast_list = []
    forecast_list.append(f"Here's the weather in {response.get('title')}")
    for i in range(1,6):
        date = response["consolidated_weather"][i]['applicable_date']
        weather_text = response["consolidated_weather"][i]['weather_state_name']
        temp_text = round(response["consolidated_weather"][i]['max_temp'], 1)
        forecast_list.append(f"{date}: {weather_text} {temp_text}°C")
    return forecast_list

if __name__ == '__main__':
    print(weather_forecast())