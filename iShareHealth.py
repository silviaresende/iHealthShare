
#from src.MyGeoMap import *
#from src.MyBarChart import *
from src.MyUserLocation import *
import sys
from urllib.request import urlopen
import json 
import plotly.express as px
import pandas as pd



myUserLocation = MyUserLocation(sys.argv[1])
print('User State value:',myUserLocation.user_state)
print('User County value:',myUserLocation.user_county)

## Initializing Map for user state
#myMap = MyMap(myUserLocation.user_state)
#myBarChart = MyBarChart(sys.argv[1])


#print('cmd entry:', sys.argv, type(sys.argv[1]))




#myUserLocation.getStateUser()
