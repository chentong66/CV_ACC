from matplotlib import pyplot as plt
import numpy as np
from scipy import signal 
import sys
import numpy as np
from PyEMD import EMD,Visualisation,EEMD
from find_near import find_near
def print_datainfo(data):
    print('mean   '+str(np.mean(data)))
    print('max    '+str(np.max(data)))
    print('min    '+str(np.min(data)))
    print('std    '+str(np.std(data)))
    print('mean-std '+str((np.mean(data)-np.std(data))))
def filter_data(data,samplefreq=200,low=2.0,high=5.0,step=3):
    data=data-np.mean(data)
    wn1 = (low / (samplefreq / 2))
    wn2 = (high / (samplefreq / 2))
    print(wn1,wn2)
    b,a = signal.butter(step,[wn1,wn2],"bandpass")
    fdata = signal.filtfilt(b,a,data)
    return fdata
def _emd_plot(imfs,residue,t):
    vis=Visualisation()
    vis.plot_imfs(imfs=imfs,residue=residue,t=t,include_residue=True)
    vis.plot_instant_freq(t,imfs=imfs)
    vis.show()
def _emd_data(data,plot,eemd=False):
    t=np.arange(0,data.shape[0],1)
    if eemd==False:
        emd=EMD()
        emd.emd(data)
        imfs,res=emd.get_imfs_and_residue()
    else:
        components=EEMD()(data)
        imfs,res=components[:-1],components[-1]
    if plot==True:
        _emd_plot(imfs,res,t)
def emd_data(data,plot=True):
    _emd_data(data,plot)
def eemd_data(data,plot=True):
    _emd_data(data,plot,eemd=True)

def erase_near_point(data,length):
    dlength=len(data)
    ret=[]
    ret.append(data[0])
    for i in range(1,dlength):
        if abs(data[i] - ret[-1]) >= length:
            ret.append(data[i])
    return np.array(ret)
def plot_data(data,count=1):
    dcolours=["b","r"]
    colours=["ks","gs"]
    for inx,val in enumerate(data):
        if inx<count:
            plt.plot(val,dcolours[inx])
        else:
            plt.plot(val,data[0][val],colours[inx-count])
    plt.show()
if __name__ == '__main__':
#    if len(sys.argv) == 3 and sys.argv[2] == 'binary':
#        data=np.load(sys.argv[1])
#        data=data.reshape((1,data.shape[0] * data.shape[1]))[0]
#        fdata=data
#        print(data.shape)
#        print(data)
#    else:
    data=np.loadtxt(sys.argv[1])
    fdata=filter_data(data,low=2.0,high=5.0)
#    fdata=data
#    fdata = fdata - np.mean(fdata)
#    fdata = np.abs(fdata)
    print_datainfo(fdata)
#    fdata = find_near(fdata,barrier=0.043)
    x=np.arange(0,fdata.shape[0])
    y=fdata[x]
    plt.plot(x,y)
    plt.show()

