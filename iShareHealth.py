
#from src.MyGeoMap import *
#from src.MyBarChart import *
from src.MyUserLocation import *
import sys
#from urllib.request import urlopen
#import json 
from src.MyMap import *
from  src.MyBar import * 
from src.MyTrends import *

## User informed its zipcode: provide costumized information for its area.
if len(sys.argv)>1: 
    
    ## User input zipcode
    print('===============================')
    print('User zipcode: ', sys.argv[1])
    print('===============================')
    
    # Getting user State and County codes
    myUserLocation = MyUserLocation(sys.argv[1])

    print('User State FIP Code: ', myUserLocation.user_state)
    print('User County FIP Code: ', myUserLocation.user_county)
    print('User State Name: ', myUserLocation.user_state_name)
    print(' ')

    ## Initializing Charts from  user inputs
    print('=====================================')
    print('Initializing Charts from  user inputs')
    print('=====================================')
    map = MyMap(myUserLocation.user_state, myUserLocation.user_state_name)
    bar = MyBar(myUserLocation.user_state, myUserLocation.user_state_name)
    trend = MyTrends(myUserLocation.user_state, myUserLocation.user_state_name)
    
    

## User didn't inform Zipcode: provide overview of national cases.
else:
    ## Get the trends f123456
    #  US cases in tehe last 3 or 6 months (maybe a year).
    print("")

print("End of iShareHealth.py script Execution")

