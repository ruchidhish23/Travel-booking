# Travel-booking

Steps follwed to create a travel assisting chatbot:
1. A new folder Travel was created
2. Under this folder a new file named travel.py was created. 
3. After that, new virtual environment was created (trasa) using cmd prompt from the terminal, in which Scripts was activated.
4. Then we came out of the folder by using cd .. , cd .. and then installed rasa and initialized it.
5. Then trained rasa on various examples and entered the actions to train it.



Codes:

# Created folder Travel > new file > travel.py
- in terminal under cmd prompt
> python -m venv trasa
> cd trasa
> cd Scripts
> activate
> cd ..
> cd ..
> pip install rasa
> rasa init       # initializing rasa
>
> under data > nlu.yml - enter intents and example
> domain.yml - enter intents, actions, entities, responses
> under data > stories.yml - create story by entering intent - action format
> actions.py - create class for actions
> rasa train
# open another cmd 
> rasa run actions
# reopen the previous cmd where rasa train was executed
> rasa shell
# give inputs 
> /stop
> ctrl + c       # in the other cmd 
