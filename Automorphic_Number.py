n=int(input())
a=len(str(n))
c=n*n
lastdigit=c%pow(10,a)
if lastdigit==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
