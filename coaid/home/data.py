import requests
from datetime import datetime
from .models import Active_cases, Death_cases, Covid_tests, updateinfo

def Get_Data():
    url = "https://covid-193.p.rapidapi.com/history"
    querystring = {"country":"India","day":"2021-05-28"}
    headers = {
        'x-rapidapi-key': "bf5d549a77mshbc72405cd326346p1a22f9jsn9520774b3508",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    mydict = {"time":"","date":"","active":"","critical":"","new":"","recovered":"","total_case":"","total_death":""}
    mydict["time"]=data["response"][0]["time"][11:19]
    mydict["date"]=data["parameters"]["day"]
    mydict["active"]=data["response"][0]["cases"]["active"]
    mydict["critical"]=data["response"][0]["cases"]["critical"]
    mydict["new"]=data["response"][0]["cases"]["new"][1:]
    mydict["recovered"]=data["response"][0]["cases"]["recovered"]
    mydict["total_case"]=data["response"][0]["cases"]["total"]
    mydict["total_death"]=data["response"][0]["deaths"]["total"]
    return mydict

def Post_Data():
    mydict = Get_Data()

    Active = Active_cases()
    Active.date = datetime.strptime(mydict['date'], "%Y-%m-%d")
    Active.active = mydict['active']
    Active.critical = mydict['critical']
    Active.new = mydict['new']
    Active.recovered = mydict['recovered']
    Active.total = mydict['total_case']
    Active.save()

