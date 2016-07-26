f=open("USIP",'r')
out=open("nonpeakhourcdf",'w')
for ip in f:
    try:
        p=open(ip.rstrip()+".out",'r')
        for line in p:
            if (int(line.split()[1].split(":")[0]) < 16):
                ping=line.split()[2]
                out.write(ping+"\n")
        p.close()
    except:
        pass
f.close()
out.close()
