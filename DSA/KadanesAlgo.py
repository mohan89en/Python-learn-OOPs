def maxSubArraySum(arr,N):
        ma_x = arr[0]
        cur = 0
        for i in range(0,N):
            cur = cur+arr[i]
            if(cur>ma_x):
                ma_x = cur
            if(cur<0):
                cur = 0
        return ma_x
    
cha = [1,2,3,4,5,6,7,8,9,10]

print(maxSubArraySum(cha,len(cha)))