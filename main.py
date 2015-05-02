from flask import Flask
from flask.ext.cors import CORS
from flask import jsonify
import subprocess
from Server import *
app = Flask(__name__)
cors = CORS(app)

@app.route("/api/server")
def getAll():
    cpu = Server.getCPUtemp().copy()
    cpu.update(Server.getCPUusage())
    memory = Server.getMemInfo()
    hdd = Server.getHDDinfo() 
    up = Server.getUptime()
    return jsonify(cpu=cpu, memory=memory, harddrives=hdd, uptime=up)

@app.route("/api/server/temp")
def getCPUTemp():
    temp = Server.getCPUtemp()
    return jsonify(temp)


@app.route("/api/server/cpu")
def getCPUUsage():
    usage = Server.getCPUusage()
    return jsonify(usage)

@app.route("/api/server/memory")
def getMEMStatus():
    memory = Server.getMemInfo()
    return jsonify(memory)

@app.route("/api/server/hdd")
def getHDDStatus():
    hdd = Server.getHDDinfo()
    return jsonify(harddrives=hdd)

@app.route("/api/server/uptime")
def getUptime():
    uptime = Server.getUptime()
    return jsonify(uptime)


if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8081)
