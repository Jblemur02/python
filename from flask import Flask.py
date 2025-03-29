from flask import Flask
app = Flask("turkey")
@app.route("/")
def home():
    return "Hello, Flask!"
-\