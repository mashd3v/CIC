def inserta(x,lst,i):
  # Devuelve una lista resultado de insertar x en la posiciòn i
  return lst[:i]+[x]+lst[i:]

def inserta_multiple(x,lst):
  # Devuelve una lista con el resultado de insertar x en todas las posiciones de lst
  return [inserta(x,lst,i) for i in range(len(lst)+1)]

def permuta(c):
  # Calcula y devuelve una lista de todas las permutaciones posibles que se pueden hacer con los 
  # elemntos   contenidos en c
  if len(c)==0:
    return [[]]
  return sum([inserta_multiple(c[0],i) for i in permuta(c[1:])],[])

def sgn(p):
  # Cuenta el nùmero de inversiones en una permutaciòn a y calcula su  signo
  count=0;i=-1;a=[]
  for k in range(len(p)):
    a=a+[p[k]]
  while i<len(a)-2:
    i=i+1
    if a[i]>a[i+1]:
      aux=a[i];a[i]=a[i+1];a[i+1]=aux
      count=count+1
      i=-1
      continue
  if count%2==0:
    return 1
  return -1

def det(a):
  # Calcula el determinante de la matris a 
  n=len(a)
  s=range(n)
  t=permuta1(s)
  d=0
  for u in t:
    r=sgn(u)
    for i in range(n):
      r=r*a[i,u[i]]
    d=d+r
  return d

def permuta1(c):
  # Calcula y devuelve una lista de todas las permutaciones posibles que se pueden hacer con los 
  # elemntos   contenidos en c
  if len(c)==0:
    return [[]]
  lst=[]
  for i in permuta1(c[1:]):
    lst=lst+inserta_multiple(c[0],i)
  return lst


  


  


