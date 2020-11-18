import numpy as np
def detect_minmax(data,length=120):
    ret=[]
    for i in range(0,data.shape[0] - length + 1):
        minmax=np.max(data[i:i+length-1]) - np.min(data[i:i+length-1])
        ret.append(minmax)
    return np.array(ret)

def detect_smooth(_data,length):
    data=np.copy(_data)
    data_length=len(data)
    inx=0
    while inx < data_length:
        inx=inx+1
        val=data[inx]
#        end_tmp = inx + length;
        if inx > 0:
            try:
                if data[inx-1] >= val and data[inx+1] <= val:
                    i = inx+1
#                    for i in range(inx+1,inx+length+1):
                    while i >= inx + 1 and i <= inx+length:
                        try:
                            p = data[i]
#                            if p >= val and p <= data[inx-1]:
                            if p >= data[inx] and p <= data[inx-1]:
                                for j in range(inx,i):
                                    data[j] = p
#                                break
                            i=i+1
                        except:
                            break
            except:
                break
    return data


def detect_avg_minmax(data,length=120):
    ret=[]
    hlength = length / 2 
    for i in range(0,hlength):
        ret.append(0)
    for i in range(hlength,data.shape[0] - hlength + 1):
        minmax=np.max(data[i-hlength:i+hlength-1]) - np.min(data[i-hlength:i+hlength-1])
        ret.append(minmax)
    for i in range(data.shape[0] - hlength + 1,data.shape[0]):
        ret.append(0)
    return np.array(ret)

def detect_avg_minmax1(data,length=120):
    ret=[]
    hlength = length / 2 
    for i in range(0,hlength):
        ret.append(0)
    for i in range(hlength,data.shape[0] - hlength + 1):
        ndata = data[i]
        tdata = data[i-hlength:i+hlength-1]
        mean = np.mean(tdata)
        mul = 10 / mean
        tdata = tdata - np.mean(tdata)
        tdata = (tdata * mul)
        tdata = np.sum(tdata)
        ret.append(tdata)
    for i in range(data.shape[0] - hlength + 1,data.shape[0]):
        ret.append(0)
    return np.array(ret)

def detect_soft(data,length=120,stdmul=3,zerostd=True):
    ret=[]
    hlength = length / 2 
    for i in range(0,hlength):
        ret.append(0)
    for i in range(hlength,data.shape[0] - hlength + 1):
        ndata = data[i]
        tdata = data[i-hlength:i+hlength-1]
        mean = np.mean(tdata)
        std = stdmul * (np.std(tdata,ddof=1))
        ndata = ndata - mean
        if ndata < std and ndata > -std and zerostd:
            ndata = 0
        ret.append(ndata)
    for i in range(data.shape[0] - hlength + 1,data.shape[0]):
        ret.append(0)
    return np.array(ret)


def detect_square_minmax(data,length=120):
    ret=[]
    hlength = length / 2 
    for i in range(0,hlength):
        ret.append(0)
    for i in range(hlength,data.shape[0] - hlength + 1):
        ndata = data[i]
        tdata = data[i-hlength:i+hlength-1]
        tmean = np.mean(tdata)
        square_minmax = (ndata - tmean) * 10000
        square_minmax = square_minmax * square_minmax
#        minmax=np.max(data[i-hlength:i+hlength-1]) - np.min(data[i-hlength:i+hlength-1])
        ret.append(square_minmax)
    for i in range(data.shape[0] - hlength + 1,data.shape[0]):
        ret.append(0)
    return np.array(ret)


