from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/dadjoke")
def get_random_dad_joke():

    response = requests.get("https://icanhazdadjoke.com/",
                            headers={"Accept": "application/json"})

    if response.status_code == 200:
        joke = response.json()["joke"]
        return jsonify({"joke": joke})

    else:
        return jsonify({"error": "Failed to retrieve random dad joke."}), 500
