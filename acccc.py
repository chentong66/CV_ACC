import numpy as np
import sys
from matplotlib import pyplot as plt
def calc_acc(data,h=float(1)):
    dlen = data.shape[0]
    acc=[]
    acc.append(0.0)
    acc.append(0.0)
    acc.append(0.0)
    for i in range(3,dlen-3):
        f0=data[i]
        f1=data[i+1]
        f2=data[i+2]
        f3=data[i+3]
        b1=data[i-1]
        b2=data[i-2]
        b3=data[i-3]
        print(4*f0+(f1+b1)-2*(f2+b2)-(f3+b3))
        acc.append(float((4*f0+(f1+b1)-2*(f2+b2)-(f3+b3))/(16*h*h)))
    acc.append(0.0)
    acc.append(0.0)
    acc.append(0.0)
    return np.array(acc)
a=np.loadtxt(sys.argv[1])
b=calc_acc(calc_acc(calc_acc(a)))
b=np.abs(b)
x=np.arange(0,b.shape[0])
y=b[x]
plt.plot(x,y)
plt.show()

