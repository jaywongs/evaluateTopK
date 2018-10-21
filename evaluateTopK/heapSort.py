import sys
import time
import heapq

def topKHeap (array, k):
    heapArr = array[0: k]
    heapq.heapify(heapArr)
    for i in range(k, len(array), 1):
        if array[i] > heapArr[0]:
            heapArr[0] = array[i]
            heapq.heapify(heapArr)
    heapArr.sort(reverse=True)
    return heapArr

if __name__== "__main__":
    start = time.clock()
    array = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line.find(".") == -1:
                array.append(int(line))
            else:
                array.append(float(line))
    k = int(array.pop(0))
    if k < 5:
        array = topKHeap(array, k)
    else:
        array = heapq.nlargest(k, array)

    result = ""
    for i in range(k - 1):
        result += str(array[i]) + ','
    result += str(array[k - 1])
    print("堆排序2算法耗时：", time.clock() - start)
    print(result)
