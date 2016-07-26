f=open("USIP",'r')
out=open("nonpeakhourcdfweekday",'w')
out2=open("nonpeakhourcdfweekend",'w')
weekday=[1,2,3]
weekend=[4,5]
for ip in f:
    try:
        
        p=open(ip.rstrip()+".out",'r')
        
        for line in p:
            #print int(line.split()[0].split("-")[2])
            if int(line.split()[0].split("-")[2]) in weekday:
                #print "weekday"
                if (int(line.split()[1].split(":")[0]) >=18 or int(line.split()[1].split(":")[0])<8):
                    ping=line.split()[2]
                    out.write(ping+"\n")
            elif int(line.split()[0].split("-")[2]) in weekend:
                #print "weekend"
                if (int(line.split()[1].split(":")[0]) >=18 or int(line.split()[1].split(":")[0])<8):
                    ping=line.split()[2]
                    out2.write(ping+"\n")
        p.close()
    except:
        pass
f.close()
out.close()
out2.close()
