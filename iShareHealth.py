
## Importing Libraries

import sys
import streamlit as st
import psycopg2
from sqlalchemy import create_engine, text
from flask import Flask, request, jsonify

from src.MyMap import *
from src.MyBar import * 
from src.MyTrends import *
from src.MyUserLocation import *
from src.MyConnection import *


## Creating local database connection
conn = MyConnection.getMyConnection()
# engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')
#conn = engine.connect() 

# engine = psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="_healthshare123",
#     host="healthshare.crpizus8bidb.us-east-2.rds.amazonaws.com",
#     port='5432'
#         )

st.cache_data(ttl=600)
st.header(".: iHealthShare :. ")
st.write("Getting Data Analysis for User Location")

## At this point you can choose using a Streamlit app or not!
user_input = st.text_input('Please enter your location (Zipcode): ', max_chars = 8)
#user_input = sys.argv[1]

if len(user_input)>1: 
    
    ## User input zipcode
    print('===============================')
    print('User zipcode: ', user_input)
    print('===============================')

    # Getting user State and County codes
    print('=====================================')
    print('Getting user State and County codes')
    print('=====================================')
    
    myUserLocation = MyUserLocation(user_input,conn)  # myUserLocation = MyUserLocation(user_input)#sys.argv[1])
    
    print('User State FIP Code: ', myUserLocation.user_state)
    print('User County FIP Code: ', myUserLocation.user_county)
    print('User State Name: ', myUserLocation.user_state_name)
    print(' ')

    ## Initializing Charts from  user inputs
    print('=====================================')
    print('Initializing Charts')
    print('=====================================')
    
    conn = MyConnection.getMyConnection()
    map = MyMap(myUserLocation.user_state, myUserLocation.user_state_name, conn)
    path_to_html = "./images/myMap.html" 

    # Reading HTML file and putting into variable
    with open(path_to_html,'r') as f: 
        html_data = f.read()

    ## Putting html file into a webpage component
    st.write("Covid-19 Cases in your State ")
    st.components.v1.html(html_data,height=400)

    ## Associating an image file to a webpage component
    bar = MyBar(myUserLocation.user_state, myUserLocation.user_state_name, conn)
    st.write("Top 5 Cases by Counties ")
    st.image("./images/myBarChart.png")
    
    ## Associating an image file to a webpage component
    trend = MyTrends(myUserLocation.user_state, myUserLocation.user_state_name,conn)
    st.write("Trends for Over Last Six Months ")
    st.image("./images/myTrends.png")
    
    print('=====================================')
    print('                Done                 ')
    print('=====================================')

    conn.close()


## User didn't inform Zipcode: provide overview of national cases.
else:
    ## Get the trends f123456
    #  US cases in tehe last 3 or 6 months (maybe a year).
    conn.close()
    print("No ZipCode was found")