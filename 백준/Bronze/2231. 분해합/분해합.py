a = int(input())
b = max(1,a-54)
answer = 0

for i in range(b,a):
    c = i
    length = len(str(i))
    for j in range(length):
        c += int(str(i)[j])
    
    if c == a:
        answer = i
        break
    else:
        pass
    
print(answer)