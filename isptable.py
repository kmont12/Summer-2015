import pygeoip,subprocess
gi = pygeoip.GeoIP('GeoIPISP.dat')
f=open("USIP",'r')
isp=[]
clients=[]
allclients=0
for ip in f:
    try:
        org=gi.org_by_addr(ip.rstrip())
        if  org in isp:
            i=isp.index(gi.org_by_addr(ip.rstrip()))
            clients[i]+=1            
        else:
            isp.insert(0,org)
            clients.insert(0,1)
    except:
        print " l"
print len(isp), len(clients)

out=open("ISPtable",'w')

for i in range(len(isp)):
    try:
        #print isp[i], client[i]
        out.write(isp[i] +" & "+ str(clients[i]) + " \\\\ \n")
    except:
        out.write("Unknown & "+str(clients[i])+" \\\\\n")
out.close()
f.close()

for item in clients:
    allclients+=item
print allclients
