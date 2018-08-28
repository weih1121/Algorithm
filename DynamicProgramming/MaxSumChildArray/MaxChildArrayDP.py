"""
DP求解最大子数组和问题
该问题可以理解为，某一项的最大前缀值为整个数组的子数组求和中最大的
存在：a[i] 使得 a[n] + ... + a[i] >= sum(sub(arr)p)(
    即：从arr的子数组中任取一项的值均小于或等于以i为结尾的数组的最大前缀的值)
"""
def maxChildArrDP(arr):
    dp = [arr[0]]
    for i in range(1, len(arr)):
        if dp[i - 1] + arr[i] >= arr[i]:
            dp.append(dp[i - 1] + arr[i])
        else:
            dp.append(arr[i])
    return max(dp)

if __name__ == '__main__':
    arr = [1, -2, 3, -10, -4, 7, -2, -5]
    maxSubArr = maxChildArrDP(arr)
    print(maxSubArr)
