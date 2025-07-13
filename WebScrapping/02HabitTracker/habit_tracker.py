import requests
from datetime import datetime

# user_yr = int(input("Year: [Input must be like '2024']: "))
# user_mo = int(input("Month : [Input must be like '01' for january]: "))
# user_date = int(input("Day: [Input must be like '01']: "))
# user_walk = str(input("You Have Walked Today For : [In Km]: "))

# date = datetime(year= user_yr, month= user_mo, day= user_date)


PIXELA_USER = "https://pixe.la/v1/users"
TOKEN = "***********"

user_params = {
    "token" : TOKEN,
    "username" : "soumyo",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# 

PIXELA_GRAPH = f"{PIXELA_USER}/{user_params['username']}/graphs"
graph_params = {
    "id" : "graph2",
    "name" : "Walk Tracker Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai",
}


headers = {
    "X-USER-TOKEN" : TOKEN
}



PIXELA_TRACKING = f"{PIXELA_USER}/{user_params['username']}/graphs/{graph_params['id']}"

# track_params = {
#     "date" : date.strftime("%Y%m%d"),
#     "quantity" : user_walk
# }

# response = requests.post(url= PIXELA_TRACKING, json= track_params, headers=headers)
# print(response.text)

PIXELA_UPDATE = f"{PIXELA_USER}/{user_params['username']}/graphs/{graph_params['id']}/20241102"

update_pixel_data = {
    "quantity" : "10.24"
}

response = requests.put(url= PIXELA_UPDATE, json= update_pixel_data, headers=headers)
print(response.text)


