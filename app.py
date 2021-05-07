from flask import Flask, jsonify
import json

from helpers import data_file_name
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_space_data():
    with open(f"data/{data_file_name()}.json", "r", encoding="utf8") as json_file:
            data = json.load(json_file)
            json_file.close()
            return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


app.run()