import random
from time import time


# Set random seed
random.seed(42)



randomDataRange = 100_000_000
nDataList = 10_000_000

arrayRandom = []
print("Prepare random sorted list")
for a in range(randomDataRange):
    if len(arrayRandom) > 0:

        # print("Value randomg {:d} value Before {:d}".format(random.randint(arrayRandom[-1],nDataList),arrayRandom[-1]))
        # print()
        # # check wheter data is equi or not,
        value = random.randint(arrayRandom[-1],nDataList) if arrayRandom[-1] > random.randint(arrayRandom[-1],nDataList) else random.randint(arrayRandom[-1],(nDataList:=nDataList+100))
        arrayRandom.append(value)
    else:

        arrayRandom.append(random.randint(0,nDataList))


randomValueExistInList = arrayRandom[random.randint(0, len(arrayRandom)-1)]
print("Banyak Data {:,}".format(len(arrayRandom)))
print("Nilai dicari {:d}".format(randomValueExistInList))
print("-"*5)

def linearSarch(array, value):
    for a in array:
        if a == value:
            return a
        
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # Target not found


# Waktu sekarang
print("Linear Search")
now = time()
print("Hasil ",linearSarch(arrayRandom, randomValueExistInList))
print("Estimasi Waktu : {:.10f} ".format(time() - now))

print("")
print("Binary Search")
now2 = time()
print("Hasil ",arrayRandom[binary_search(arrayRandom, randomValueExistInList)])
print("Estimasi Waktu : {:.10f} ".format(time() - now2))