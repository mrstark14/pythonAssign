a=list()
for x in range(0,5):
    a1 = list(map(int, input().split()))
    a.append(a1)
b,c=0,0
for x in range(0,5):
    for y in range(0,5):
        if(a[x][y]==1):
            b,c=x,y
print(abs(b-2)+abs(c-2))