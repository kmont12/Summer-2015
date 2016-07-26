f=open("USpairIP",'r')
out=open("allcdf",'w')
for pair in f:
    ip=pair.split("'")[1]
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
