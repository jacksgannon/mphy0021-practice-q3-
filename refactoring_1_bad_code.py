from numpy import *
import matplotlib.pyplot as plt

xrange = 500
yrange = 500

A = zeros([yrange,xrange])
for x in range(xrange):
    for y in range(yrange):
        zx=1.5*(x-xrange/2)/(0.5*1*xrange)
        zy=1.0*(y-yrange/2)/(0.5*1*yrange)
        i=255
        t=True
        while t==True:
            if zx*zx+zy*zy>=4:
                t=False
            if i<=1:
                t=False
            a=zx*zx-zy*zy-0.7
            zy=2.0*zx*zy+0.27015
            zx=a
            i=i-1
        A[y][x]=i
plt.imshow(A)
plt.show()
