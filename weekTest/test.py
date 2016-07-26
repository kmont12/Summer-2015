import subprocess
from geoip  import geolite2
t=[]
def getTimeDif(ip):
        td=0
        try:
                match = geolite2.lookup(ip.rstrip()).timezone.split("/")[1]
                if match =="New_York" or match =="Indiana":
                        td=4
                elif match =="Los_Angelos" or match=="Phoenix" :
                        td=7
                elif match =="Chicago":
                        td=5
                elif match =="Denver":
                        td=6
                elif match =="Anchorage":
                        td=8
                return td
        except:
                return 5.5
if __name__=="__main__":
        f=open("USIP",'r')
        for ip in f:
                if type(getTimeDif(ip))==str:
                        print getTimeDif(ip)

        f.close()



