import sys
out=open("PairIP",'r')
l=[]
for line in out:
    l.append(line.rstrip())
out.close()

f=open(sys.argv[1],'r')
out=open("PairIP",'w')


for line in f:
    inlist=False
    for item in l:
        if line.rstrip() == item:
            inlist=True
    if not inlist:
        l.append(line.rstrip())
print len(l)
for item in l:
    out.write(item+"\n")
out.close()
f.close()
