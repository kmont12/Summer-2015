f=open("UIP",'r')
out=open("cdf",'w')
for line in f:
    inp=open(line.rstrip()+".out",'r')
    for item in inp:
        out.write(item.rstrip()+"\n")
    inp.close()
f.close()
out.close()
