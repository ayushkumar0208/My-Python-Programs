def binary_search(l,low,high,val):
    if(high<low):
        return None
    else:
        midval=(low+high)//2
    if(l[midval]>val):
        return binary_search(l,low,midval-1,val)
    elif(l[midval]<val):
        return binary_search(l,midval+1,high,val)
    else:
        return midval
l=[1,22,333,24,3,5,66,990]
print(binary_search(l,0,7,990))
print(binary_search(l,0,7,34))
print(binary_search(l,0,4,5))
print(binary_search(l,0,7,24))














