import os, time, math, tempfile, subprocess
import numpy
check_output=subprocess.check_output
chdir=os.chdir

try:
    import Gnuplot, Gnuplot.PlotItems, Gnuplot.funcutils
except ImportError:
    # kludge in case Gnuplot hasn't been installed as a module yet:
    import __init__
    Gnuplot = __init__
    import PlotItems
    Gnuplot.PlotItems = PlotItems
    import funcutils
    Gnuplot.funcutils = funcutils

g=Gnuplot.Gnuplot(debug=1)
arr=["akamai","cloudfront", "edgecast"]
for item in arr:
    f=open(item,'r')
    c=0
    for line in f:
        c+=1
    g.set_range("yrange", (.95,1))
    g.set_range("xrange", (-1,5))
    g.plot("\""+item+"\" u 1:(1./"+str(c)+") smooth cumulative notitle lw 5")
    g.title("United States "+item+" CDF")
    g.set_label("xlabel","Download Time-1")
    g.set_label("ylabel", "CDF")
    g.hardcopy("US-CDF"+item+".png", terminal="png")
    g.replot()
