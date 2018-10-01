def getNextList(p_arr):
    nextList = [0, 0]    #匹配不成功的时候直接返回getList的结果，不用往前看一位（好像是。。。）
    j = 0
    for i in range(1, len(p_arr)):
        while j>0 and p_arr[i] != p_arr[j]:
            j = nextList[j]               #回到上一个和前面字符匹配成功的位置
        if p_arr[i] == p_arr[j]:
            j += 1
        
        nextList.append(j)
        print(p_arr[i], nextList)
    
    return nextList


def KMP(p_arr, s_arr):
    sl = len(s_arr)
    pl = len(p_arr)
    nextList = getNextList(p_arr)
    j = 0
    res = []
    for i in range(0, sl):
        while j>0 and s_arr[i] != p_arr[j]:
            j = nextList[j]
        
        if s_arr[i] == p_arr[j]:
            j += 1
            if j == pl:
                print(i ,j)
                res.append(i-pl+1)
                j = nextList[j]             #  最开始有匹配成功的那就从匹配成功的地方继续开始
    return res


if __name__ == '__main__':
    s_arr = "BBC ABCDAB ABCDABCDABDE"
    p_arr = "ABCDABD"
    print(KMP(p_arr, s_arr))