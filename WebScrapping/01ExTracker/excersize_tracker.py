import requests
import datetime as dt

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
print(date, time)

NUIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUIX_KEY = "84944806744f901ab2cc2125c95ac953"
NUIX_ID = "869ef8b7"

headers = {
    "x-app-key" : NUIX_KEY,
    "x-app-id" : NUIX_ID
}

params = {
    "query" : "I ran for 44.89 mins"
}

response = requests.post(url=NUIX_URL, json= params, headers=headers)
data = response.json()
print(data)
ex_name = data['exercises'][0]['name']
ex_duration = data['exercises'][0]['duration_min']
ex_cal = data['exercises'][0]['nf_calories']
print(ex_name, ex_cal, round(ex_duration))

SHEETY_URL = "https://api.sheety.co/06b767c4600edfff8f846ce4ed639aae/workoutTracking/workouts"

infos = {
    "workout" : {
        "Date" :date,
        "Time" :time,
        "Exercise" :ex_name,
        "Duration" :ex_duration,
        "Calories" : ex_cal
    }
}

headers2 = {
    "Authorization" : "Basic"
}

response2 = requests.post(url=SHEETY_URL, params=infos, headers=headers2)
print(response2.text)