import os, time
import socket
from threading import Thread
import SocketServer, subprocess
try:
    check_output = subprocess.check_output
except AttributeError:
    def check_output(*popenargs, **kwargs):
        if 'stdout' in kwargs:
            raise ValueError('stdout argument not allowed, it will be overridden.')
        process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            raise CalledProcessError(retcode, cmd, output=output)
        return output

files=[]
num=0
def ping(ip):
    out=open(ip+".out",'a')
    try:
        response = check_output("ping -c 1 "+ ip +" | grep from", shell=True).split("=")[3].split()[0]
    except:
        response=""
    try:
        r=float(response)
        out.write(response+"\n")
    except:
        pass
    out.close()

if __name__=="__main__":
    f=open("UIP")
    os.chdir("Jun17")
    for i in range(100):
        f.seek(0,0)
        for line in f:
                t=Thread(target=ping,args=(line.rstrip(),))
                t.Daemon=True
                t.start()
                time.sleep(.01)
        time.sleep(1800)
        

