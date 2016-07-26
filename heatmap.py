from geoip import geolite2
f=open("USIP",'r')
out=open("heat.txt",'w')

l=[]
n=[]

for line in f:
    match=geolite2.lookup(line.rstrip())
    try:
        state=str(match.subdivisions).split("'")[1]
        print state
        if state in l:
            i=l.index(state)
            n[i]+=1
        else:
            l.insert(0,state)
            n.insert(0,1)              
    except:
        pass
print len(l), len(n)


for i in range(len(l)):
    out.write(l[i]+ "\t" +str(n[i])+"\n")
out.close()
f.close()
