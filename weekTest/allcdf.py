f=open("USIP",'r')
out=open("allcdf",'w')
count=0
for ip in f:
    try:
        p=open(ip.rstrip()+".out",'r')
        for line in p:
            count+=1
            ping=line.split()[2]
            out.write(ping+"\n")
        p.close()
    except:
        pass
print count
f.close()
out.close()
