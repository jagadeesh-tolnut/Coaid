# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def Get_Data():
    import requests
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

class ActionActiveCase(Action):

    def name(self) -> Text:
        return "action_active_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = Get_Data()
        return_data = "Today's Covid active cases are " + str(data["active"])
        dispatcher.utter_message(text=return_data)
        return []

class ActionRecoverCase(Action):

    def name(self) -> Text:
        return "action_recover_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = Get_Data()
        return_data = "Today's Covid recoverd cases are " + str(data["recovered"])
        dispatcher.utter_message(text=return_data)
        return []

class ActionNewCase(Action):

    def name(self) -> Text:
        return "action_new_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = Get_Data()
        return_data = "Today's newly added covid cases are " + str(data["new"])
        dispatcher.utter_message(text=return_data)
        return []
