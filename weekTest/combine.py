f1=open("peakhourcdfweekday",'r')
f2=open("peakhourcdfweekend",'r')
out=open("peak",'w')

for line in f1:
    out.write(line)
for line in f2:
    out.write(line)
f1.close()
f2.close()
out.close()
