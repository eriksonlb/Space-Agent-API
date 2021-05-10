from flask import Flask, jsonify
import json

from helpers import data_file_name, events_data
import os

print('starting...')
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_space_data():
    events_data()
    with open("data/events.json", "r", encoding="utf8") as json_file:
            data = json.load(json_file)
            json_file.close()
            return jsonify(data)




app.run()