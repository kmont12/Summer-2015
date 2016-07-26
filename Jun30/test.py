import pygeoip,subprocess
gi = pygeoip.GeoIP('GeoIPISP.dat')
f=open("USIP",'r')
for line in f:
    print gi.org_by_addr(line.rstrip())


