n = int(input())

result = 0
for _ in range(n):
  st = input()
  if st.count('OI') >= 1 or st.count('01') >= 1:
    result += 1
print(result)