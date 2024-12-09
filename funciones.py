#Generar emojis aleatorios 

import random

def gen_emoji():

    #lista de emojis 

    emojis = [
    "\U0001f600", 
    "\U0001f601", 
    "\U0001f602", 
    "\U0001f603", 
    "\U0001f604",
    "\U0001f605", 
    "\U0001f606", 
    "\U0001f607", 
    "\U0001f609", 
    "\U0001f60A",
    "\U0001f60B",
    "\U0001f60D", 
    "\U0001f618", 
    "\U0001f622", 
    "\U0001f62D",
    "\U0001f621", 
    "\U0001f631", 
    "\U0001f642", 
    "\U0001f923", 
    "\U0001f970"
]


    emoji = random.choice(emojis)

    return emoji

print(gen_emoji())