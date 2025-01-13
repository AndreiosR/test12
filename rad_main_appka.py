# Importing all app imports
from config import *

# Main Window Functions
def prepocet_CML(weight,activityfactor):
    bmr=weight*24.2
    cml=bmr*activityfactor
    cmlrounded= round(cml, 1)
    return cmlrounded

def mesto_backend(mesto):
    mesto=text_a
    if mesto == "Brno":
        text_a="Pokračujte v moravském jazyce"
    elif mesto == "Wien":
        text_a="Geht ihr weiter in deutsche Sprache, bitte!"
    elif mesto == "Bratislava":
        text_a="Slováci rozumí moravsky..."
    return text_a


# Main Window Variables
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Main Window Lists / Dictionaries
