from geoip import geolite2

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
                return 5


if __name__=="__main__":
    f=open("USIP",'r')
    out=open("nonpeak",'w')
    out2=open("peak",'w')
    count=0
    for ip in f:
        try:
            p=open(ip.rstrip()+".out",'r')
            td=getTimeDif(ip)
            upbound=18-td
            lowbound=8-td
            if lowbound<0:
                lowbound+=24
            for line in p:
                count+=1
                if (int(line.split()[1].split(":")[0]) >=upbound or int(line.split()[1].split(":")[0])<lowbound):
                    ping=line.split()[2]
                    out.write(ping+"\n")
                else:
                    ping=line.split()[2]
                    out2.write(ping+"\n")

            p.close()
        except:
            pass
    print count
    f.close()
    out.close()
    out2.close()

