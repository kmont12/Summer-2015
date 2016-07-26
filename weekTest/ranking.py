import os
LIP=open("USIP",'r')
out=open("rankings",'w')
percent=[]
numclients=[]
c=[]

for ip in LIP:
    count=False
    ip=ip.rstrip()
    try:
        f=open(ip+".out",'r')
    except:
        f=open(ip+".out",'w')
        f.close()
        f=open(ip+".out",'r')
    if os.stat(ip+".out").st_size !=0:
        count=True
    miss=0
    for line in f:
        ping=float(line.split()[2])
        count+=1
        if ping>80:
            miss+=1
    f.close()
    coverage=miss
    if coverage in percent:
        i=percent.index(coverage)
        numclients[i]+=1
    else:
        percent.insert(0,coverage)
        numclients.insert(0,1)
        c.insert(0,count)
for i in range(len(percent)):
    for j in range(len(percent)-1):
        if percent[i]>percent[j]:
            temp1=percent[j]
            temp2=numclients[j]
            temp3=c[j]
            percent[j]=percent[i]
            numclients[j]=numclients[i]
            c[j]=c[i]
            percent[i]=temp1
            numclients[i]=temp2
            c[i]=temp3

for x in range(len(percent)):
    for i in range(numclients[x]):
    	out.write("\""+str(x)+"\" \t"+str(percent[x])+"\n")
LIP.close()
out.close()
        
