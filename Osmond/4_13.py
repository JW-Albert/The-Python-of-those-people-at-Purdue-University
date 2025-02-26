def average(b):
    sum=0
    for i in b:
        sum+=i
    
    leng=0
    for i in b:
        leng+=1
    
    return sum/leng

a=list(map(int,input().split()))
if len(a)==0:
    print("NO")
else:
    print(average(a))