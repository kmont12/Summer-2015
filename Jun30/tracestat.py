import os

f=open("USIP",'r')
out=open("traces",'w')
total=0
msource=0
mcore=0
mdest=0
trace=[]
for ip in f:
    try:
        p=open("trace/" +ip.rstrip()+".trace",'r')
        line=p.readline()
        while line !="":
            ls=line.split()
            if ls[0]=="traceroute":
                trace.insert(0,[ip.rstrip()])
                line=p.readline()
                ls=line.split()
                ping=0
                count=0
                for i in range(1,len(ls)):
                    try:
                        ping +=float(ls[i].rstrip())
                        count+=1
                    except:
                        pass
            else:
                ping=0
                count=0
                for i in range(1,len(ls)):
                    try:
                        ping +=float(ls[i].rstrip())
                        count+=1
                    except:
                        pass
            if count>0:
                trace[0].append(ping/count)
            line=p.readline()
        p.close()
    except:
        pass
for item in trace:
    ip=item[0]
    maxRtt=0
    inUse=False
    for c in range(1,len(item)):
        if item[c]>maxRtt:
            maxRtt=item[c]
            inUse=True
    if inUse:
        out.write(ip+" "+str(item.index(maxRtt)) +" "+ str(len(item)-1) +" "+ str(maxRtt) +"\n")
out.close()
f.close()
        
                        
                        
                        
        
    

