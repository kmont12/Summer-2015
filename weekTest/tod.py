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
    out=open("timeofday",'w')
    tod=[]
    tlat=[]
    tot=[]
    for ip in f:
        ip=ip.rstrip()
        try:
            p=open(ip+".out",'r')
        except:
            p=open(ip+".out",'w')
            p.close()
            p=open(ip+".out",'r')
        for line in p:
            date=line.split()[0].split("-")[2]
            time=int(line.split()[1].split(":")[0])-getTimeDif(ip)
            if time<0:
                time+=24
                date=str(int(date)-1)
            #print time
            identifier=date+"-"+str(time)
            if identifier in tod:
                i=tod.index(identifier)
                tlat[i]+=float(line.split()[2])
                tot[i]+=1
            else:
                tod.insert(0,identifier)
                tlat.insert(0,float(line.split()[2]))
                tot.insert(0,1)
        p.close()


    for i in range(len(tod)):
        for j in range(len(tod)-1):
            if int(tod[i].split("-")[0]) <= int(tod[j].split("-")[0]) and int(tod[i].split("-")[1]) <= int(tod[j].split("-")[1]):
                tmptod=tod[j]
                tmptlat=tlat[j]
                tmptot=tot[j]
                tod[j]=tod[i]
                tlat[j]=tlat[i]
                tot[j]=tot[i]
                tod[i]=tmptod
                tlat[i]=tmptlat
                tot[i]=tmptot

    ##tod.reverse()
    ##tlat.reverse()
    ##tot.reverse()
    for i in range(len(tod)):
        print tod[i], tlat[i]/tot[i]
        if int(tod[i].split("-")[1])==0:
            out.write("\""+tod[i].split("-")[0]+"\" \t"+ str(tlat[i]/tot[i])+"\n")
        else:
            out.write("\"\"\t"+str(tlat[i]/tot[i])+"\n")
    f.close()
    out.close()

