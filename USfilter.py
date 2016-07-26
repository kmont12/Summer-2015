from geoip import geolite2
f=open("PairIP",'r')
out=open("USpairIP",'w')
count=0
badcount=0
notUS=0
for item in f:
    try:
        match = geolite2.lookup(item.split("'")[1])
        if match.country=="US":
            out.write(item.rstrip()+"\n")
            count+=1
        else:
            notUS+=1
    except:
        badcount+=1
        
print count, badcount, notUS
f.close()
out.close()

