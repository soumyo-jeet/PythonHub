import requests
import os
import datetime as dt
from twilio.rest import Client

acc_sid = os.getenv("ACCOUNT_SID")
print(acc_sid)
acc_token = ""


now_hour = dt.datetime.now().hour

respose = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=-4.441931&lon=15.266293&appid=ccb0ca5a60c3e24fa0ecaa85bc4382c8&cnt=4")

data = respose.json()
print(data["list"][0]["weather"][0]["id"])

raining = False
for each in data["list"]:
    check_val = each["weather"][0]["id"]
    # time_bound = each["dt_txt"].split(" ")[1].split[":"][0]
    print(check_val)
    if check_val < 700 :
        raining = True
        time = each["dt_txt"].split(" ")[1]
        break

if raining:
    print(f"Bring an Umbrella! It's probable to rain on {time}")
    client = Client(acc_sid, acc_token)
    msg = client.messages.create(body=f"Bring an Umbrella! It's probable to rain on {time}", from_="+19046010428", to="+918910048803")
    print(msg.status)



