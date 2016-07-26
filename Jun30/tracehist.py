mcore=0
ms=0
md=0
u=0
preip=""
total=0.0
f=open("traces",'r')
out=open("tracestat",'w')
for line in f:
    total+=1
    ls=line.split()
    if int(ls[2])-int(ls[1])>1:
        if int(ls[1])<2:
            ms+=1
        else:
            mcore+=1
    else:
        if preip != ls[0]:
            p=open("trace/"+ls[0]+".trace",'r')
            pre=""
            for trace in p:
                first=True
                ts=trace.split()
                if ts[0]=="traceroute":
                    if pre == ls[0]:
                        md+=1
                    elif pre != "":
                        u+=1
                else:
                    pre=ts[2].split(")")[0].lstrip("(")
            p.close()
            preip=ls[0]
total = float(ms+mcore+md+u)
out.write("\"Source Issue\"\t" +str(ms/total*100)+"\n")
out.write("\"Core Issue\"\t"+ str(mcore/total*100)+"\n")
out.write("\"Destination Issue\"\t"+str(md/total*100)+"\n")
out.write("\"Unknown Issue\"\t"+str(u/total*100))
out.close()
f.close()
