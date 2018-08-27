def maxChildArray(arr):
    lenArr = len(arr)
    maxLocation = [[-9999999999999, 0, 0]]                #数据由3个子项构成，最大值，起点，长度
    for i in range(lenArr):                               #取数据-第i轮 第i轮取i + 1个数据
        for j in range(lenArr):                           #从哪个位置开始取数据
            tmp = 0
            if j + i <= lenArr - 1:                       #判断索引是否越界
                for k in range(j, j + i + 1):             #range(j, j + i + 1)从第j个开始取数据，额外可以取i个， j + i + 1取不到
                    tmp += arr[k]                         #求和未使用sum()函数，是因为不想对原数组进行切片操作，需占用额外空间
                if tmp > maxLocation[0][0]:
                    maxLocation.clear()
                    maxLocation.append([tmp, j, i + 1])
                elif tmp == maxLocation[0][0]:
                    maxLocation.append([tmp, j, i + 1])
    return maxLocation

def maxChildArrayBin

if __name__ == '__main__':
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    # arr = [1, 2, -100, 1, 2, -92929, 0, 0, 0, 1, 2]
    res = maxChildArray(arr)
    print(res)
    No = 0
    for item in res:
        print("第{}组: max:{}".format(No, item[0]))
        No += 1
        for i in range(item[1], item[2] + item[1]):
            print(arr[i])


            