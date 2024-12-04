n = 7
m = 21
pat = '.|.'
j = n//2 -1
for i in range(n):
  if i == n//2:
    print('WELCOME'.center(m,'-'))
  elif i <n//2:
    print((pat*(2*i+1)).center(m,'-'))
  else:
    print((pat*(2*j+1)).center(m,'-'))
    j-=1
    
