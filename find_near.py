from matplotlib import pyplot as plt
import numpy as np
from scipy import signal 
import sys
def find_near(data,barrier=0.04):
    length=data.shape[0]
    lists=[]
    for i in range(0,length):
        if data[i] > barrier:
            lists.append(data[i])
        else:
            lists.append(0)
    return np.array(lists)
if __name__ == '__main__':
    if len(sys.argv) >= 2:# and sys.argv[2] == 'binary':
        data=np.loadtxt(sys.argv[1])
#        data=data.reshape((1,data.shape[0] * data.shape[1]))[0]
        fdata=find_near(data,0.000002)
        print(data.shape)
        print(data)
#data=data-np.mean(data)
    x=np.arange(0,fdata.shape[0])
    y=fdata[x]
    plt.plot(x,y)
    plt.show()

