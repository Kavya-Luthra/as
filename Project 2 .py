#                                                                          PROJECT DATA ANALYTICS

print("                                                                     DATA ANALYTICS TOOLS                                                                 ")



#                                           pyttsx3 Library   Work = (Speaking Text)

import pyttsx3 as tt

engine = tt.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hello world")
engine.runAndWait()

engine.say("wellcom to our new PROJECT DATA ANALYTICS")
engine.runAndWait()


import matplotlib as plt 
a = []