f=open("USpairIP",'r')
out=open("peakhourcdf",'w')
for pair in f:
    ip=pair.split("'")[1]
    try:
        p=open(ip.rstrip()+".out",'r')
        for line in p:
            if (int(line.split()[1].split(":")[0]) > 16 and int(line.split()[1].split(":")[0])<24):
                ping=line.split()[2]
                out.write(ping+"\n")
        p.close()
    except:
        pass
f.close()
out.close()
