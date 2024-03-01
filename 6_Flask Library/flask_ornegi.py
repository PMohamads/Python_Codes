from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/merhaba")
def merhaba():
    return "<p>Hello!</p>"\

@app.route("/merhaba/dunya")
def dunya():
    return "<p>Hello dunya!</p>"

if __name__=="__main__":
    app.run(debug = True ,host="localhost",port=22222)