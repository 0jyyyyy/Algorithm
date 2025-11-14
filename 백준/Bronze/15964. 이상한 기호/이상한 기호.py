def a_b(a,b):
  result = (a+b)*(a-b)
  return result

a,b = map(int,input().split())

anb = a_b(a,b)
print(anb)