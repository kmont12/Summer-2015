import os

f=open("usIP",'r')
os.chdir("BrewTest")
cdf=open("cdf",'w')
for line in f:
    os.chdir(line.rstrip())
    out=open(line.rstrip()+".out",'r')
    for ping in out:
        if ping !="":
            cdf.write(ping.rstrip()+"\n")
    os.chdir("..")
        
