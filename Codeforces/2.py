a=int(input())
a1 = list(map(int, input().split()))
a1.sort(reverse=True)
sum = sum(a1)
x=0
y=0
while(y<=sum//2):
    y+=a1[x]
    x+=1
print(x)