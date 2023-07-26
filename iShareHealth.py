
from src.MyGeoMap import *
#from src.MyBarChart import *
from src.MyUserLocation import *
import sys
#from urllib.request import urlopen
#import json 

## User informed its zipcode: provide costumized information for its area.
if len(sys.argv)>1: 

    ## User inserted zipcode
    print('User ZipCode:', sys.argv, type(sys.argv[1]))
    
    # Getting user State and County codes
    myUserLocation = MyUserLocation(sys.argv[1])
    print('User State code value:', myUserLocation.user_state)
    print('User County code value:', myUserLocation.user_county)

    ## Initializing Map for user state
    myMap = MyGeoMap(myUserLocation.user_state)
    #myBarChart = MyBarChart(sys.argv[1])
    
    myUserLocation.getStateUser()

## User didn't inform Zipcode: provide overview of national cases.
else:
    ## Get the trends for US cases in tehe last 3 or 6 months (maybe a year).
    print("")

print("End of iShareHealth script Execution")
