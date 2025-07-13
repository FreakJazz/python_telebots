from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/joke")
def joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    if response.status_code == 200:
        data = response.json()
        chiste = f"{data['setup']} {data['punchline']}"
    else:
        chiste = "No hay chiste"
    
    return jsonify({"joke":chiste})
                    

if __name__ == "__main__":
    app.run(debug=True)