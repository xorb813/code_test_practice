import sys

input = sys.stdin.readline

a,b = map(int,input().split())
nums = list(map(int,input().split()))
max_num = -1

for i in range(a):
    num1 = nums[i]
    for j in range(i+1,a):
        num2 = nums[j]
        for k in range(j+1,a):
            num3 = nums[k]
            criterion = num1 + num2 + num3
            if criterion > max_num and criterion <= b:
                max_num = criterion
            else:
                pass
            
print(max_num)