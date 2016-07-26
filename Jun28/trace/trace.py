f=open("USIP",'r')
out=open("numHops",'w')
for ip in f:
    try:
        p=open(ip.rstrip()+".trace",'r')
        count=0
        for line in p:
            ls=line.split()
            if ls[0]=="traceroute":
                #print "begin"
                if count !=0:
                    print "write"
                    out.write(str(count)+"\n")
                    count=0
            else:
                #print "+1"
                count+=1
        out.write(count+"\n")
        p.close()
    except:
        pass
f.close()
out.close()
        
