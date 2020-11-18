from matplotlib import pyplot as plt
import numpy as np
from scipy import signal 
import sys
from find_near import find_near
def filter_data(data,samplefreq=200,low=2.0,high=10.0,step=3):
    wn1 = (low / (samplefreq / 2))
    wn2 = (high / (samplefreq / 2))
    print(wn1,wn2)
    b,a = signal.butter(step,[wn1,wn2],"bandpass")
    fdata = signal.filtfilt(b,a,data)
    return fdata
if __name__ == '__main__':
    count=len(sys.argv)
    data=np.load(sys.argv[1])
#    data=np.abs(dat)
    print(data.shape)
    if count==3 and (sys.argv[2]=='max' or sys.argv[2]=='min'):
        print(sys.argv)
        lenx=data.shape[0]
        leny=data.shape[1]
        minmax=0
        if sys.argv[2]=='min':
            minmax=1
        print(minmax)
        padding=list(np.zeros(leny))
        l1=[]
        l2=[]
        for ary in data:
            print(np.max(ary)-np.min(ary))
            if minmax==0:
                num=np.max(ary)
            else:
                num=np.min(ary)
            if num==0:
                continue
            l1.append(num)
            l2.append(num)
            l1=l1+padding
        data=np.array(l1)
        datatmp=np.array(l2)
        print(datatmp)
        print('mean,min,max,std,mean-std:')
        print(np.mean(datatmp),np.min(datatmp),np.max(datatmp),np.std(datatmp),np.mean(datatmp)-np.std(datatmp))
        print(datatmp.shape)
        datatmp=datatmp<(np.mean(datatmp)-np.std(datatmp))
        print(datatmp)
        print(datatmp.sum())
    else:
        data=data.reshape((1,data.shape[0] * data.shape[1]))[0]
    x=np.arange(0,data.shape[0])
    y=data[x]
    plt.plot(x,y)
    plt.show()

