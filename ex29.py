import math


def vsphere(r,h):
    result = ( ( 4 * math.pi *  math.pow(r,3) ) / 3 ) - ( math.pi * float( math.pow(h,2) * ( 3*r - h ) ) )/3
    return result


print(vsphere(10,2))
