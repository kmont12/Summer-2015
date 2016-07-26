f1=open("ISPtable",'r')
f2=open("statisp",'r')

out1=open("ISPlist",'w')
out2=open("ispstat",'w')


isp=[]
numclients=[]
for line in f1:
    name=line.split("&")[0].rstrip()
    num=line.split()[-2]
    isp.insert(0,name)
    numclients.insert(0,num)

print len(isp), len(numclients)
for line in f2:
    if line.split("\"")[1] in isp:
        print "happen"
        i=isp.index(line.split("\"")[1])
        if int(numclients[i]) >5:
            out1.write(isp[i]+" & "+ numclients[i]+" \\\\ \n")
            out2.write(line)
f1.close()
f2.close()
out1.close()
out2.close()
