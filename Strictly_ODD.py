a=int(input())
b=[int(x) for x in input().split()]
c=[]
d=0
for i in (range(len(b))):
    if i%2!=0 and b[i]%2!=0:
        d=d+1
for i in b:
    if i%2!=0:
        c.append(i)
if d>=len(c):
    print(True)
else:
    print(False)