import subprocess
import os, sys, json, math

class Server:

    @staticmethod
    def getCPUtemp():
	temp = subprocess.check_output("sensors | grep 'Core 1'", shell=True)[17:21]
        return dict(temperature=temp)

    @staticmethod
    def getCPUusage():
        cpuUsage = subprocess.check_output("top -d 0.5 -b -n2 | grep 'Cpu(s)'|tail -n 1 | awk '{print $2 + $4}'", shell=True).rstrip('\n')
        return dict(usage=cpuUsage)

    @staticmethod
    def getMemInfo():
	memtotal = subprocess.check_output("cat /proc/meminfo | grep MemTotal | sed 's/ //g'", shell=True)[9:16]
     	memfree = subprocess.check_output("cat /proc/meminfo | grep MemFree | sed 's/ //g'", shell=True)[8:14]
	return dict(total=memtotal, free=memfree)
    
    @staticmethod
    def getHDDinfo():
	bak = disk_usage("/media/bak")
   	one = disk_usage("/media/#1")
   	c = disk_usage("/")
	return [bak, one, c]

    @staticmethod
    def getUptime():
	up_time = subprocess.check_output("cut -d. -f1 /proc/uptime", shell=True).rstrip('\n')
   	up_time = float(up_time)
    	days = int(math.floor(up_time / 60 / 60 / 24))
    	hrs = int(up_time / 60 / 60 % 24)
    	mins = int(up_time / 60 % 60)
    	secs = int(up_time % 60)
	return dict(days=days, hours=hrs, mins=mins, secs=secs)


def disk_usage(path):
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return dict(hdd=path, free=free, total=total, used=used)
