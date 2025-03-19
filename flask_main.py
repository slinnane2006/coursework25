from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

#This tells flask to run the app on your computers IP (incase others might want to connect to it)
app.run(host='0.0.0.0', port=5899, debug=False)
