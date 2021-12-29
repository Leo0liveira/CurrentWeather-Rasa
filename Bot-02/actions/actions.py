# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient
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
        response = requests.get(url).json()
        
        try:
            format = response['main'] 
            temp = int(format['temp']) 
            place = response["name"] 
            format = response['weather'] 
            desc = format[0]['description'] 
            weather_data = "Neste momento está fazendo {}°C na cidade de {}, o tempo é {}. Obrigado por escolher nosso serviço {} 😊. ".format(temp, place, desc, nome) 
            
            client = MongoClient('mongodb+srv://leo:1234@cluster0.ga9of.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
            
            db = client['database']
            collection = db['historico']
            insertDB = [{"nome": nome, "city": city, "response" : response}]
            
            collection.insert_many(insertDB)
            
            dispatcher.utter_message(weather_data) 
            
        except:
            dispatcher.utter_message(text=f"Desculpe {nome}, mas parece que a cidade de {city} não é válida, tente novamente.")
                
        finally:
            return [SlotSet("location", None)]
    
# class ActionShowHistory(Action):
    
#     def name(self) -> Text:
#         return "action_show_history"
    
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         for response in collection.find():
#             history_data = "O usuario {} buscou pela cidade de {}. ".format(nome, city)
#             dispatcher.utter_message(history_data)

#         return []