from math import sqrt

def div(n):
  s = set([1])
  for r in range(2, int(sqrt(n))+1):
    if n % r == 0:
      s.add(r)
      s.add(n/r)
  return sum(s)

ab = set(i for i in range(1,30000) if div(i) > i)
ss = set(x+y for x in ab for y in ab)
zs = set(range(1,28124))
print sum(zs - ss)