"""
分治法：
    left:左边最大值
    right:右边最大值
    post + pre: 最大后缀 + 最大前缀
    最大值: max(left, right, post + pre)
"""
import math

def maxArraySub(arr, from_, to):
    print('from: {}, to: {}'.format(from_, to))
    if from_ == to:
        return arr[to]
    mid = math.floor((from_ + to)/2)
    left = maxArraySub(arr, from_, mid)
    right = maxArraySub(arr, mid + 1, to)

    postLeft = now = arr[mid]
    for i in range(mid - 1, from_ - 1, -1):
        now += arr[i]
        postLeft = max(now, postLeft)

    preRight = now = arr[mid + 1]
    for i in range(mid + 2, to + 1):
        now += arr[i]
        preRight = max(now, preRight)

    print(left, right, postLeft, preRight)
    return max(left, right, postLeft + preRight)


if __name__ == '__main__':
    arr = [1, -2, 3, 10, -4, 7, -2, -5]
    res = maxArraySub(arr, 0, len(arr) - 1)
    print(res)


    