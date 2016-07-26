import os
f=open("usIP")
os.mkdir("BrewTest")
os.chdir("BrewTest")
for line in f:
    try:
        os.mkdir(line.rstrip())
    except:
        pass
