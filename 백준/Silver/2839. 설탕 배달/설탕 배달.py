n = int(input())

# 일단 최대한 5kg을 많이 사용한 상태로 시작
count_5 = n // 5
n %= 5

while count_5 >= 0:
  if n % 3 == 0: # 남은게 3으로 나누어 떨어지면
    count_3 = n // 3
    total_count = count_5 + count_3
    print(total_count)
    exit()
  count_5 -= 1
  n += 5
# 루프가 끝날때까지 답을 찾지 못하면 -1
print(-1)