import random
import time

N=10000
lstNumbers=list(range(N))
random.seed(1)
random.shuffle(lstNumbers)

print(lstNumbers)

def selectionSort(lstNumbers):

    for iter in range(len(lstNumbers)):
        count=0
        for idx in range(len(lstNumbers)-1):
            if lstNumbers[idx]<lstNumbers[idx+1]:
                count+=1
                continue
            else:
                tmp=lstNumbers[idx]
                lstNumbers[idx]=lstNumbers[idx+1]
                lstNumbers[idx+1]=tmp
        if count==len(lstNumbers)-1:
            return lstNumbers

    return lstNumbers

start=time.time()
print(selectionSort(lstNumbers)) #17.778438568115234
end=time.time()
print(end-start)