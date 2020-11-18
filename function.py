import numpy as np
import sys
import numpy as np
from scipy import signal 
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

def load_data(path):
    try:
        fdata=np.load(path)
    except:
        try:
            fdata=np.loadtxt(path)
        except:
            fdata = None
    return fdata

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


def find_above(data,barrier=0.04):
    length=data.shape[0]
    lists=[]
    for i in range(0,length):
        if data[i] > barrier:
            lists.append(data[i])
        else:
            lists.append(0)
    return np.array(lists)


def _get_data_(data,start,end):
    ret=data[start:end]
    return ret
def __get_near_data__(data,point,num,forward,backward):
    datalength = len(data)
    if forward == True and backward == True:
        num = num / 2
        start=point-num
        end=point+num
    elif forward == True:
        start=point-num
        end=point
    else:
        start=point
        end=point+num
    if start < 0 or end > datalength:
        success = False
        ret = None
    else:
        success = True
        ret=_get_data_(data,start,end)
    return success,ret

def _get_near_data_(data,point,num):
    return __get_near_data__(data,point=point,num=num,forward=True,backward=True)

def get_near_data(data,points,num,debug=False,padding=False):
    ret=[]
    for point in points:
        point = point + 50
        success,pdata=_get_near_data_(data,point=point,num=num)
        if success == False:
            continue
        ret.append(list(pdata))
        if padding == True:
            pads = np.zeros((pdata.shape[0]))
            print("Padding")
            ret.append(list(pads))
        if debug == True:
            print("Point:{0}".format(point))
            print("Datas:{0}".format(pdata))
#    print(ret)
    return np.array(ret)



