from flask import Flask, request
from markupsafe import escape
import json

app = Flask(__name__)

# Fonction pour lire les données du fichier JSON
def read_counter():
    with open("counter.json", "r") as f:
        data = json.load(f)
    return data

# Fonction pour écrire les données dans le fichier JSON
def write_counter(data):
    with open("counter.json", "w") as f:
        json.dump(data, f)

@app.route("/counter")
def counter():
    data = read_counter()
    data["counter"] += 1
    render_number = data["counter"]
    write_counter(data)
    return f"You are visitor number {render_number}"

@app.route("/ip")
def ip():
    user_ip = request.remote_addr
    return f"Votre adresse IP est : {user_ip}"