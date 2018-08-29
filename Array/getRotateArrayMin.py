"""
有序数集合旋转之后，获取集合中的最小值
解法：
1.一次遍历就不说了
2.用二分法求解降低时间复杂度O(logn)
"""
import math

def getRotateArrMinRecur(arr, from_ , to):
    if from_ == to:
        print(arr[to])

    mid = math.floor((from_ + to) / 2)
    if arr[mid] > arr[to]:
        from_ = mid + 1
    elif arr[mid] < arr[to]:
        to = mid
    getRotateArrMinRecur(arr, from_, to)

def getRotateArrMin(arr):
    from_, to = 0, len(arr) - 1
    while from_ < to:
        mid = math.floor((from_ + to) / 2)
        if arr[mid] > arr[to]:
            from_ = mid + 1
        elif arr[mid] < arr[to]:
            to = mid
        print(from_, to)
    return arr[to]


if __name__ == '__main__':
    arr0 = [4, 5, 6, 7, 1, 2, 3]
    arr1 = [6, 7, 8, 1, 2, 3, 4, 5]
    res = getRotateArrMin(arr0)
 