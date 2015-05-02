from flask import Flask
from flask.ext.cors import CORS
from flask import jsonify
import subprocess
app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/server/temp")
def getCPUTemp():
    temp = subprocess.check_output("sensors | grep 'Core 1'", shell=True)[17:21]
    return jsonify(temperature=temp)


@app.route("/api/server/cpu")
def getMEMUsage():
    cpuUsage = subprocess.check_output("top -b -n 2 -d .5 | grep Cpu", shell=True)
    cpus = cpuUsage.split('Cpu(s):')
    for c in cpus:
        total = c[0:4]
    print total
    return total


if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8081)
