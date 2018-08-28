"""
DP求解最大子数组和问题
该问题可以理解为，某一项的最大前缀值为整个数组的子数组求和中最大的
存在：a[i] 使得 a[n] + ... + a[i] >= sum(sub(arr)p)(
    即：从arr的子数组中任取一项的值均小于或等于以i为结尾的数组的最大前缀的值)
"""
def maxChildArrDP(arr):
    dp = [arr[0]]                           #此处使用数组仍然具有可以优化的空间
    for i in range(1, len(arr)):
        if dp[i - 1] + arr[i] >= arr[i]:
            dp.append(dp[i - 1] + arr[i])
        else:
            dp.append(arr[i])
    return max(dp)

#通过使用pre记录前一项的最大前缀和，和当前变量作比较，滚动记录前一项最大前缀和，无需开辟n长空间
#优化空间
def maxChildArrDPOpti(arr):
    pre = arr[0]            #记录前一个最大前缀
    sum = arr[0]            #记录最终结果

    for i in range(1, len(arr)):
        if pre + arr[i] >= arr[i]:
            pre = arr[i] + pre
        else:
            pre = arr[i]
        sum  = pre if pre >= sum else sum
    return sum


if __name__ == '__main__':
    arr = [1, 2, 3, -10, -4, 7, -1, 2, -5]
    maxSubArr = maxChildArrDPOpti(arr)
    print(maxSubArr)
