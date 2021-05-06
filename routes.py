from flask import Flask

from web_scrapping import get_data

app = Flask("Space Agent")

@app.route("/data", methods=["GET"])
def get_space_data():
    return get_data()


app.run()