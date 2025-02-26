def b(n):
    if n<1:
        return 0
    
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=i
    
    if c==n:
        return 1
    else:
        return 0
a=int(input())

if b(a):
    print("YES")
else:
    print("NO")