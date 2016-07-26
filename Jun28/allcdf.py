f=open("USIP",'r')
out=open("allcdf",'w')
for ip in f:
    try:
        p=open(ip.rstrip()+".out",'r')
        for line in p:
            ping=line.split()[2]
            out.write(ping+"\n")
        p.close()
    except:
        pass
f.close()
out.close()
