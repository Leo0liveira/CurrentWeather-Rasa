# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

import requests

class ActionWeatherApi(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nome = tracker.get_slot("name")
        city = tracker.get_slot('location')
        
        api_address = 'http://api.openweathermap.org/data/2.5/weather?units=metric&appid=0c42f7f6b53b244c78a418f4f181282a&lang=pt_br&q='
        url = api_address + city 
        json_data = requests.get(url)
        
        data = json_data.json()
        
        format = data['main']
        temp = int(format['temp'])
        place = data["name"]
        format = data['weather']
        desc = format[0]['description']
    
        weather_data = "Neste momento está fazendo {}°C na cidade de {}, o tempo é {}. Obrigado pela preferência {}. ".format(temp, place, desc, nome)
        dispatcher.utter_message(weather_data)
       
        return [SlotSet("location", city)]