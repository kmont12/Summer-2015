f=open("ISPtable",'r')
f1=open("Jun30/statisp",'r')
out=open("realISP",'w')
l=[]
for line in f1:
    isp=line.split("\"")[1]
    l.append(isp)

for line in f:
    isp=line.split("&")[0].rstrip()
    if isp in l:
        print line
        out.write(line)

out.close()
f.close()
f1.close()
