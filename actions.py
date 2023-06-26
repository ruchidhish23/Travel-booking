# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Hello World!")

        return []

# This action is created the beginning of the travel booking chats 
class ActionTravelBooking(Action):

    def name(self) -> Text:
        return "action_travel_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        dispatcher.utter_message(text="Welcome to our travel agency! How may I help you?")

        return []

# flight_booking action is created for the user to get a response from the chatbot so that the user can take actions accordingly.      
class ActionFlightBooking(Action):

    def name(self) -> Text:
        return "action_flight_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        message = "Please mention the cities"

        dispatcher.utter_message(text="Here is the link from where you can book the tickets.\nhttps://www.easemytrip.com/")

        return []

# Likewise hotel_booking action was created    
class ActionHotelBooking(Action):

    def name(self) -> Text:
        return "action_hotel_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        message = "Please mention the cities"

        dispatcher.utter_message(text="Please click on the link for hotel booking.\nhttps://www.agoda.com/")

        return []