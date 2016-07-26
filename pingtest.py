import os, time
import socket
from threading import Thread
import SocketServer, subprocess
import datetime



class Node:

    ip=""
    out=None

    def __init__(self, address):
        self.ip=address


    def ping(self):
        for i in range(48):
            
            try:
                response = subprocess.check_output("ping -c 1 "+ self.ip.rstrip() +" | grep from", shell=True).split("=")[3].split()[0]
            except:
                response=""
            try:
                r=float(response)
		st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                out=open(self.ip+".out",'a')
                out.write(st+" "+response+"\n")
                out.close()
                if r>80:
                    subprocess.call("traceroute "+self.ip.rstrip()+">> "+self.ip.rstrip()+".trace",shell=True)
                
            except:
                pass
            
            time.sleep(1800)

if __name__=="__main__":
    f=open("USIP")
    os.chdir("Jun28")
    for ip in f:
        to=Node(ip.rstrip())
        t=Thread(target=to.ping,args=())
        t.Daemon=True
        t.start()
        time.sleep(.01)


        
