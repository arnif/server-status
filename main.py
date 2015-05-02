from flask import Flask
from flask.ext.cors import CORS
from flask import jsonify
from collections import namedtuple
import subprocess
import os, sys, json, math
from Server import *
app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/server")
def getAll():
    f = Server.test(22)
    print type(f)
    return jsonify(number=f)

@app.route("/api/server/temp")
def getCPUTemp():
    temp = Server.getCPUtemp()
    print temp
    return jsonify(temp)


@app.route("/api/server/cpu")
def getCPUUsage():
    cpuUsage = subprocess.check_output("top -d 0.5 -b -n2 | grep 'Cpu(s)'|tail -n 1 | awk '{print $2 + $4}'", shell=True).rstrip('\n')
    return jsonify(usage=cpuUsage)

@app.route("/api/server/memory")
def getMEMStatus():
    memtotal = subprocess.check_output("cat /proc/meminfo | grep MemTotal | sed 's/ //g'", shell=True)[9:16]
    memfree = subprocess.check_output("cat /proc/meminfo | grep MemFree | sed 's/ //g'", shell=True)[8:14]
    return jsonify(total=memtotal, free=memfree)

@app.route("/api/server/hdd")
def getHDDStatus():
    bak = disk_usage("/media/bak")
    one = disk_usage("/media/#1")
    c = disk_usage("/")
    return jsonify(harddrives=[bak, one, c])

@app.route("/api/server/uptime")
def getUptime():
    up_time = subprocess.check_output("cut -d. -f1 /proc/uptime", shell=True).rstrip('\n')
    up_time = float(up_time)
    days = int(math.floor(up_time / 60 / 60 / 24))
    hrs = int(up_time / 60 / 60 % 24)
    mins = int(up_time / 60 % 60)
    secs = int(up_time % 60)
    return jsonify(days=days, hours=hrs, mins=mins, secs=secs)

def disk_usage(path):
    """Return disk usage statistics about the given path.

    Returned valus is a named tuple with attributes 'total', 'used' and
    'free', which are the amount of total, used and free space, in bytes.
    """
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return dict(hdd=path, free=free, total=total, used=used)

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8081)
