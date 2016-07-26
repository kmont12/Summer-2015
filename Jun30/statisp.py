import pygeoip,subprocess
gi = pygeoip.GeoIP('GeoIPISP.dat')
f=open("USIP",'r')
isp=[]
misses=[]
attempts=[]
for ip in f:
    try:
        p=open(ip.rstrip()+".out",'r')
        if  gi.org_by_addr(ip.rstrip()) in isp:
            i=isp.index(gi.org_by_addr(ip.rstrip()))
            for line in p:
                if line!="":
                    attempts[i]+=1
                    if float(line.split()[2])>80:
                        misses[i]+=1

        else:
            isp.append(gi.org_by_addr(ip.rstrip()))
            misses.append(0)
            attempts.append(0)
            i=isp.index(gi.org_by_addr(ip.rstrip()))
            for line in p:
                if line !="":
                    attempts[i]+=1
                    if floar(line.split()[2])>80:
                        misses[i]+=1

        p.close()
    except:
        pass

out=open("statisp",'w')
for i in range(len(isp)):
    if misses[i] >0:
        out.write("\""+str(isp[i])+ "\" \t"+ str(100*float(misses[i])/attempts[i])+"\n")
    print isp[i], float(misses[i]), float(attempts[i])
out.close()
f.close()
            
