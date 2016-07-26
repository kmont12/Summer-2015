import os

os.chdir("..")
f=open("usIP",'r')
os.chdir("BrewTest")
count1=0
good=0
for ip in f:
    os.chdir(ip.rstrip())
    inp=open(ip.rstrip()+".out",'r')
    
    for n in inp:
        count1+=1
        if float(n.rstrip())<80:
            good+=1
    os.chdir("..")
print float(good)/count1
