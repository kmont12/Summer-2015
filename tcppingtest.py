import os, time, datetime
import socket
from threading import Thread
import SocketServer, subprocess



class Node:

    ip=""
    port=-1
    out=None

    def __init__(self, address, port):
        self.ip=address
        self.port=port


    def ping(self):
        for i in range(48):
            
            try:
                response = subprocess.check_output("tcpping -x 1 "+ self.ip.rstrip() + " " +str(self.port), shell=True).split()[7]
            except:
                response=""
            try:
                r=float(response)
		st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                out=open(self.ip.rstrip()+".out",'a')
                out.write(st+" "+response+"\n")
                out.close()
                if r>80:
                    subprocess.call("traceroute "+self.ip.rstrip()+">> "+self.ip.rstrip()+".trace",shell=True)
                
            except:
                pass
            
            time.sleep(1800)

if __name__=="__main__":
    f=open("USpairIP")
    os.chdir("Jun28-2")
    for line in f:
        to=Node(line.split("'")[1], line.split()[1].split(")")[0])
        t=Thread(target=to.ping,args=())
        t.Daemon=True
        t.start()
        time.sleep(.01)
    print "all started"


        
