
import shutil
from flask import Flask, request, jsonify
from src.MyUserLocation import *
from src.MyConnection import *
from src.MyMap import *
from  src.MyBar import * 
from src.MyTrends import *
from flask import send_from_directory

app = Flask(__name__)

print('Running Flask..')
conn = MyConnection.getMyConnection()
print("Connecting Database..")
print("Please open: http://127.0.0.1:5000/index.html to start using API")

@app.route("/get-user-location/<user_zipcode>")
def get_user_location(user_zipcode):
    
    myUserLocation = MyUserLocation(user_zipcode, conn)
    user_data = { 
        "user_state": myUserLocation.user_state,
        "user_county": myUserLocation.user_county,
        "user_state_name": myUserLocation.user_state_name,
    }
    
    map = MyMap(myUserLocation.user_state, myUserLocation.user_state_name, conn)
    bar = MyBar(myUserLocation.user_state, myUserLocation.user_state_name, conn)
    trend = MyTrends(myUserLocation.user_state, myUserLocation.user_state_name,conn)

    return jsonify(user_data),200


@app.route('/charts/<path:path>')
def send_report(path):
    return send_from_directory('./images', path)


@app.route("/<path:path>")
def home(path):
    return send_from_directory('./web', path)


if __name__ == "__main__":
    app.run(debug=True)
    