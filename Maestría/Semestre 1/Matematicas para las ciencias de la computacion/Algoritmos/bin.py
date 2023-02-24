def bin(x):
  if x<2:
    return [x]
  else:
    return [x%2]+bin(x//2)

def residuo(b,x,r):
  l=[]
  a=bin(x)
  n=len(a)
  for i in range(n):
    c=b%r
    l=l+[c]
    b=c*c
  s=1
  for i in range(n):
    if a[i]==1:
      s=s*l[i]
      s=s%r
  return s,l



