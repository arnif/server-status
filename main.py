from flask import Flask
from flask.ext.cors import CORS
from flask import jsonify
app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/server/temp")
def getCPUTemp():
    temp = subprocess.check_output("sensors | grep 'Core 1'", shell=True)[17:21]
    return jsonify(temperature=temp)



if __name__ == "__main__":
    app.run()
