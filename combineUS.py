f=open("USIP",'r')
l=[]
for line in f:
    l.append(line.rstrip())
f.close()

f=open("USpairIP",'r')
for line in f:
    ip=line.split("'")[1]
    inlist=False
    for item in l:
        if ip == item:
            inlist=True
    if not inlist:
        l.append(ip.rstrip())
f.close()
out=open("USIP",'w')
for item in l:
    out.write(item.rstrip()+"\n")
out.close()
