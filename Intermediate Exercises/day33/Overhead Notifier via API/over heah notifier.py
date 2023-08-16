import requests
import datetime
import pandas as pd
import smtplib
import time

LAT=29.637978
LONG=52.511785
CORRECT_ASSUMPTION=3

USERNAME='hoseinjamshidian1998@gmail.com'
PASSWORD='specific password'

#----------------------------------------------- Check Location Of ISS -----------------------------------------------
def position_right(latitude:float, longitude:float)->bool:
    req_iss = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_data = req_iss.json()
    iss_long = float(iss_data['iss_position']['longitude'])
    iss_lat = float(iss_data['iss_position']['latitude'])

    if (LAT - 5 < iss_lat < LAT + 5) and (LONG - 5 < iss_long < LONG + 5):
        return True

#----------------------------------------------- Check Night  --------------------------------------------------------
def is_night(latitude:float, longitude:float)->bool:
    global CORRECT_ASSUMPTION

    params = {
        'lat': LAT,
        'lng': LONG
    }
    req_sunrise_sunset = requests.get(url='https://api.sunrise-sunset.org/json', params=params)
    weather_data = req_sunrise_sunset.json()['results']

    sunrise = int(pd.to_datetime(weather_data['sunrise']).hour + CORRECT_ASSUMPTION)
    sunset = int(pd.to_datetime(weather_data['sunset']).hour + CORRECT_ASSUMPTION)
    # point: I've been used CORRECT_ASSUMPTION Because The Time Iformation that receive from Api is Not correct.
    my_hour = int(datetime.datetime.now().hour)

    if (sunset) < (my_hour) < (sunrise):
        return True

#----------------------------------------------- Send Mail ----------------------------------------------------------
def send_mail(username:str,password:str) :
    with smtplib.SMTP(host='smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=USERNAME,
                            to_addrs=USERNAME,
                            msg="subject:Be Hurry!!\n\nThe International Space Station (ISS) In you're Location Just Right Now!Go See The Sky!")

# ------------------------------------------------ Program Main Body ---------------------------------------------------
IS_ON=True

while IS_ON:
    time.sleep(60*60)
    if (position_right(LAT,LONG)) and (is_night(LAT,LONG)):
        send_mail(USERNAME,PASSWORD)

# TODO: check every hour (60sec*60min)