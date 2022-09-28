import json
from credentials import keys
#creating weather app
import sys
import datetime as dt
import requests

if len(sys.argv)<2:
    town=input("Choose town: ")
else:
    town=sys.argv[1]

print(sys.executable)
url="https://api.openweathermap.org/data/2.5/forecast"
parameters={"APPID":keys,"q":town}
r=requests.get(url,parameters)
weathers=r.json()
#with open("weather_forecast.txt","w")as f:   
date,time=weathers["list"][0]["dt_txt"].split()
dat=dt.datetime.strptime(date, "%Y-%m-%d")
start=dt.datetime.strftime(dat, "%d.%m.%Y")
dat1=dat+dt.timedelta(days=5)
stop=dt.datetime.strftime(dat1, "%d.%m.%Y")
print(f"Weather forecast for {town.capitalize()} from {start} to {stop}\n")
for i,items in enumerate(weathers["list"]):
    temp=items["main"]["temp"]-273.15
    w=items["wind"]["speed"]*3.6
    for description in items["weather"]:
        desc=description["description"]
    date,time=items["dt_txt"].split()
    dat=dt.datetime.strptime(date, "%Y-%m-%d")
    days=dat.weekday()
    day_of_week={0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday",
        5:"Saturday",
        6:"Sunday"}
    day=day_of_week[days]
    da=dt.datetime.strftime(dat, "%B %d, %Y")
    vrem=dt.datetime.strptime(time, "%H:%M:%S")
    vr=dt.datetime.strftime(vrem, "%H")
    if vr=="12":
        print(f"\n{da} {day}\n\n{vr}h {round(temp)}\u00B0C {round(w):>2} km/h {desc}\n")
    