from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/nazımhikmet')
def NH():
    return render_template("Nazım Hikmet.html")


@app.route('/orhanveli')
def OV():
    return render_template("Orhan Veli.html")


@app.route('/özdemirasaf')
def ÖA():
    return render_template("Özdemir Asaf.html")


app.run(host="localhost", port=5000)
