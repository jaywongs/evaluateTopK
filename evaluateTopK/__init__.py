import sys
import time
import heapq

# 未判断 脏数

def qselect(A, k):
    if len(A) < k: return A
    pivot = A[-1]
    right = [pivot] + [x for x in A[:-1] if x >= pivot]
    rlen = len(right)
    if rlen == k:
        return right
    if rlen > k:
        return qselect(right, k)
    else:
        left = [x for x in A[:-1] if x < pivot]
        return qselect(left, k - rlen) + right

def topKSort(array, k):
    start = time.clock()
    array.sort(reverse=True)
    n = len(array)
    result = ""
    for i in range(k - 1):
        result += str(array[i]) + ','
    result += str(array[i+1])
    print("快排算法耗时：", time.clock() - start)
    return result

def topKQSelect(array, k):
    start = time.clock()
    array = qselect(array, k)
    result = ""
    for num in array:
        result = str(num) + ',' + result
    print("快速选择算法耗时：", time.clock() - start)
    return result

def topKHeap(array, k):
    start = time.clock()
    heapq.heapify(array)
    n = len(array)
    result = ""
    for i in range(k - 1):
        result += str(array[n-i-1]) + ','
    result += str(array[n-i-2])
    print("堆排序1算法耗时：", time.clock() - start)
    return result

def heap_sort(ary, k):
    # 构建大顶堆
    def siftdown(ary, begin, end):
        i,j = begin, begin*2+1
        while j < end:
            if j+1 < end and ary[j+1] > ary[j]:  # 查看左右子树的最大节点
                j += 1
            if ary[i] > ary[j]:  # 如果不需要交换了，则停止
                break
            ary[i],ary[j] = ary[j],ary[i]  # 交换父和子
            i,j = j,j*2+1

    # 构建最大堆
    end = len(ary)
    for i in range(end//2-1, -1, -1):
        siftdown(ary, i, end)

    # 提取k个元素。每提取一个元素，构建一遍最大堆
    li = []
    for i in range(k):
        if len(ary) > i:
            li.append(ary[0])  # 取出最大的
            ary[end - 1 - i],ary[0] = ary[0],ary[end-1-i]  #最后一个与第一个交换。这里只是假设这么一步。
            siftdown(ary, 0, end-1-i)  # 重新建堆,不考虑最后一个
        else:
            break
    return li

def topKHeap2(array, k):
    start = time.clock()
    array = heap_sort(array, k)
    result = ""
    for i in range(k - 1):
        result += str(array[i]) + ','
    result += str(array[k-1])
    print("堆排序2算法耗时：", time.clock() - start)
    return result

def topKQuickSort(array, k):

    return

if __name__== "__main__":
    # start = time.clock()
    array = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line.find(".") == -1:
                line = int(line)
            else:
                line = float(line)
            array.append(line)
    k = int(array.pop(0))
    # sort
    print(topKSort(array, k))
    # 快速选择
    # print(topKQSelect(array, k))
    # 堆排序
    # print(topKHeap(array, k))
    # 堆排序2
    # print(topKHeap2(array, k))
