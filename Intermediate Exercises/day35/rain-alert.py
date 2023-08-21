import requests
api_key='specific api key'
OWN_endpoint='https://api.openweathermap.org/data/2.5/weather'


parameters={
    'lat':29.6036,
    'lon':52.5388,
    'appid':api_key,
    'exclude':'current,daily,minutely'
}


response=requests.get(url=OWN_endpoint,params=parameters)
response.raise_for_status()
# print(response.status_code)
weather_cond=response.json()['weather'][0]['id']
if weather_cond<700:
    print('bring an umbrella')