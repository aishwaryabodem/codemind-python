def prime(x):
    if x==1:
        return False
    for i in range(2,int((x**0.5)+1)):
        if x%i==0:
            return False
    else:
        return True
            
n=int(input())
p=int(input())
q=0
for i in range (n,p+1):
    if prime(i)==True:
        q=q+1
print(q)