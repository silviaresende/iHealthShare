
#from src.MyGeoMap import *
#from src.MyBarChart import *
from src.MyUserLocation import *
import sys
#from urllib.request import urlopen
#import json 
from src.MyMap import *
from  src.MyBar import * 
from src.MyTrends import *






# fileDownload = GoogleDrive(GoogleAuth)
# .CreateFile("https://drive.google.com/drive/folders/1b9yRDiwBhV4hc3fZtAm2vZ7kvSQJwSqX?usp=sharing")

# streamlit run simple_app.py
import streamlit as st
##

st.header("Getting data analysis for user location")
user_input = st.text_input('Please enter your location (Zipcode): ', max_chars = 8)

## User informed its zipcode: provide costumized information for its area.
#if len(sys.argv)>1: 
if len(user_input)>1: 
    
    ## User input zipcode
    print('===============================')
    print('User zipcode: ', user_input)
    #, sys.argv[1])
    print('===============================')
    # st.image('https://images-rdts.s3.us-west-2.amazonaws.com/images-2.png')

    # Getting user State and County codes
    myUserLocation = MyUserLocation(user_input)
    # myUserLocation = MyUserLocation(user_input)#sys.argv[1])
    
    print('User State FIP Code: ', myUserLocation.user_state)
    print('User County FIP Code: ', myUserLocation.user_county)
    print('User State Name: ', myUserLocation.user_state_name)
    print(' ')

    ## Initializing Charts from  user inputs
    print('=====================================')
    print('Initializing Charts from  user inputs')
    print('=====================================')
    map = MyMap(myUserLocation.user_state, myUserLocation.user_state_name, st)

    path_to_html = "./images/myMap.html" 

    # Read file and keep in variable
    with open(path_to_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.write("Covid-19 Cases in your State ")
    st.components.v1.html(html_data,height=400)




    bar = MyBar(myUserLocation.user_state, myUserLocation.user_state_name)
    st.write("Cases by Counties ")
    st.image("./images/myBarChart.png")
    # st.image("https://images-rdts.s3.us-west-2.amazonaws.com/myMap.png")
    
    trend = MyTrends(myUserLocation.user_state, myUserLocation.user_state_name)
    st.write("Trends for Over Last Six Months ")
    st.image("./images/myTrends.png")
    print('=====================================')
    
    

## User didn't inform Zipcode: provide overview of national cases.
else:
    ## Get the trends f123456
    #  US cases in tehe last 3 or 6 months (maybe a year).
    print("No ZipCode found")

