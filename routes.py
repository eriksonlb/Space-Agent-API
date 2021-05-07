from flask import Flask, jsonify
import json

from helpers import data_file_name

app = Flask("Space Agent")

@app.route("/data", methods=["GET"])
def get_space_data():
    with open(f"data/{data_file_name()}.json", "r", encoding="utf8") as json_file:
            data = json.load(json_file)
            json_file.close()
            return jsonify(data)


app.run()