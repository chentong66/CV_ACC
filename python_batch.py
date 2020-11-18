from filter_raw import *
from detect import *
from accc import calc_acc
from eye_blink_count import *
def load_data(dpath,ppath,low=1.0,high=10.0,length=200):
    a=np.loadtxt(dpath)
    orig_points=np.loadtxt(ppath,dtype=int)
    points=erase_near_point(orig_points,length)
    fdata=filter_data(a,low=low,high=high)
    adata_f=calc_acc(fdata)
    aadata_f=calc_acc(adata_f)
    adata = calc_acc(a)
    aadata = calc_acc(adata)
    return (a,orig_points,points,fdata,adata_f,aadata_f,adata,aadata)
if __name__ == '__main__':
    a=np.loadtxt("tmp/ssd/data/wuyuan/00-16-20-data.txt")
    points=np.loadtxt("tmp/p.txt",dtype=int)
    fdata=filter_data(a)
    adata=calc_acc(fdata)
    aadata=calc_acc(adata)
    #plot_data((detect_minmax(aadata,100),points))
    #quit()
    sdata=detect_smooth(detect_minmax(aadata,100),35)
    plot_data((sdata,points))
    np.savetxt("tmp/sdata.txt",sdata)
    quit()
    sdata2=detect_smooth(sdata,35)
    while not (sdata==sdata2).all():
        sdata=np.copy(sdata2)
        sdata2=detect_smooth(sdata,35)
