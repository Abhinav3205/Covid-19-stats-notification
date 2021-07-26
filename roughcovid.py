import json
import requests
from tabulate import tabulate
from plyer import notification
import datetime


url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "55bfe1d797msha90318d5e0df1a6p1067f3jsn3fd62e63f234",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }
try:
    response = requests.get(url, headers=headers)
except Exception as e:
     print("Please! Check your internet connection")

response = response.text
covid = json.loads(response)
stats = covid["state_wise"]
for states in stats:
    # print(f"State : {states}")
    statistics = stats[states]
    active = statistics["active"]
    # print(f"Active cases : {active}")
    confirmed = statistics["confirmed"]
    # print(f"Confirmed cases : {confirmed}")
    deaths = statistics["deaths"]
    # print(f"Death confirmed : {deaths}")
    recovered = statistics["recovered"]
    # print(f"Recovered : {recovered}\n")
    notification.notify(
            #title of the notification,
            title = f"COVID19 Stats on of {states} at {datetime.date.today()}" ,
            #the body of the notification
            message = f"Total cases : {active}\nTotal confirmed cases {confirmed}\nConfirmed deaths {deaths}\n Recovered {recovered}",
            app_icon = "C:\\Users\\abhin\\OneDrive\\Desktop\\python abhinav\\photo-1584036561566-baf8f5f1b144.jpg"
            ,timeout  = 5
        )
 time.sleep(60*60)
