import subprocess
import os, sys, json, math

class Server:

    @staticmethod
    def test(fo):
        return fo

    @staticmethod
    def getCPUtemp():
        temp = getSuprocessOutput("sensors | grep 'Core 1'")[17:21]
        return dict(temperature=temp)

    @staticmethod
    def getCPUusage():
        cpuUsage = getSuprocessOutput("top -d 0.5 -b -n2 | grep 'Cpu(s)'|tail -n 1 | awk '{print $2 + $4}'").rstrip('\n')
        return dict(usage=cpuUsage)



    def getSuprocessOutput(command):
        return subprocess.check_output(command, shell=True)
