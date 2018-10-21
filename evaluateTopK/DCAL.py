import sys
import time

# def sortArr(array, k):
#     sortedArr = array.sort()
#     return sortedArr[0, k]

if __name__== "__main__":
    array = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line.find(".") == -1:
                array.append(int(line))
            else:
                array.append(float(line))
    k = int(array.pop(0))
    #
    start = time.clock()
    n1 = 0
    n2 = 999
    step = 1000
    unionArr = []
    for i in range(10000):
        sortedArr = array[n1:n2]
        sortedArr.sort(reverse=True)
        for j in range(k):
            unionArr.append(sortedArr[j])
        n1 = n2 + 1;
        n2 += step
    unionArr.sort(reverse=True)
    result = ""
    for i in range(k - 1):
        result += str(unionArr[i]) + ','
    result += str(unionArr[k - 1])
    print("堆排序2算法耗时：", time.clock() - start)
    print(result)
