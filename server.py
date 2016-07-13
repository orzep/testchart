from flask import Flask, render_template, send_from_directory
import random
app = Flask(__name__)

host="0.0.0.0"
port="8080"

number = random.uniform(0, 10)
stdev = random.uniform (1.0E-3, 1.1)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/number")
def rand_num():

	return str(random.gauss(number, stdev))

@app.route("/<path:path>") 
def send_bower(path):
	return send_from_directory("", path)

if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)