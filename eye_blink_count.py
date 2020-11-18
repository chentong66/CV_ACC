import numpy as np
def __accc_detect_minmax_eye_blink_count(data,length,verbose):
    data_length=len(data)
    count=0
    inx=1
    cont_len = 0
    while inx < data_length:
        pre_val = data[inx-1]
        val = data[inx]
        if pre_val < val:
            cont_len = 1
        elif pre_val == val:
            if cont_len >= 1:
                cont_len = cont_len + 1
            else:
                cont_len =0
        else:
            if verbose==True and cont_len >= 1:
                print("In point "+str(inx-cont_len)+" continue length have "+str(cont_len))
            if cont_len >= length:
                count = count + 1
            cont_len = 0
        inx = inx + 1
    return count

def aamm_bcount(data,length,verbose=False):
    return __accc_detect_minmax_eye_blink_count(data,length,verbose)


