
#from src.MyGeoMap import *
#from src.MyBarChart import *
from src.MyUserLocation import *
import sys
#from urllib.request import urlopen
#import json 
from src.MyMap import *
from  src.MyBar import * 
from src.MyTrends import *



# streamlit run simple_app.py

import streamlit as st

st.title("Getting data for user location")
user_input = st.text_input('Please enter your zipoced: ', max_chars = 500)

## User informed its zipcode: provide costumized information for its area.
#if len(sys.argv)>1: 
if len(user_input)>1: 
    
    ## User input zipcode
    print('===============================')
    print('User zipcode: ', user_input)#, sys.argv[1])
    print('===============================')
    

    # Getting user State and County codes
    myUserLocation = MyUserLocation(user_input)#sys.argv[1])
    
    print('User State FIP Code: ', myUserLocation.user_state)
    print('User County FIP Code: ', myUserLocation.user_county)
    print('User State Name: ', myUserLocation.user_state_name)
    print(' ')

    ## Initializing Charts from  user inputs
    print('=====================================')
    print('Initializing Charts from  user inputs')
    print('=====================================')
    map = MyMap(myUserLocation.user_state, myUserLocation.user_state_name)

    path_to_html = "/Users/silviaresende/Documents/TOP/iHealthShare/images/myMap.html" 

    # Read file and keep in variable
    with open(path_to_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.header("Show an external HTML")
    st.components.v1.html(html_data,height=400)




    bar = MyBar(myUserLocation.user_state, myUserLocation.user_state_name)
    st.image("/Users/silviaresende/Documents/TOP/iHealthShare/images/myBarChart.png")
    trend = MyTrends(myUserLocation.user_state, myUserLocation.user_state_name)
    st.image("/Users/silviaresende/Documents/TOP/iHealthShare/images/myTrends.png")
    print('=====================================')
    
    

## User didn't inform Zipcode: provide overview of national cases.
else:
    ## Get the trends f123456
    #  US cases in tehe last 3 or 6 months (maybe a year).
    print("No ZipCode found")

