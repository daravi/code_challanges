def PE023(limit = 28123):
  somDiv = [1] * (limit+1) # jusk 28123 inclus
  for i in range(2, int(limit**.5)+1):
    somDiv[i*i] += i
    for k in range(i+1, limit//i+1):
        somDiv[k*i] += k+i
  abondant, res = set(), 0
  ajout = abondant.add
  for n in range(1, limit+1):
    if somDiv[n]>n: ajout(n)
    if not any( (n-a in abondant) for a in abondant ): res+=n
  return res
  
print PE023()