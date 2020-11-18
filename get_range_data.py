import sys
import numpy as np

from filter_raw import filter_data
from accc import calc_acc
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

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Usage:python get_range_data.py filter|acc|accc|raw input.txt points.txt output.txt")
        quit()
    print(sys.argv)
    raw_data=np.loadtxt(sys.argv[2])
    points=np.loadtxt(sys.argv[3]).astype(int)
    if sys.argv[1] == 'filter':
        data=filter_data(raw_data,low=2.0,high=5.0)
        data=np.abs(data)
    elif sys.argv[1] == 'accc':
        data=filter_data(raw_data,low=2.0,high=5.0)
        data=calc_acc(calc_acc(data))
    elif sys.argv[1] == 'acc':
        data=calc_acc(raw_data)
    elif sys.argv[1] == 'raw':
        data=raw_data
    rets=get_near_data(data,points,num=400,padding=True)
    print(rets)
    np.save(sys.argv[-1],rets)
#    print(len(rets[0]))
#    print(len(rets))
#    print(rets)


