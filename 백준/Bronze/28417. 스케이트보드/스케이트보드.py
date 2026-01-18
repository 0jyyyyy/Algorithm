import sys

n = int(sys.stdin.readline())
result_lst = []
result = 0
for _ in range(n):
  lst = list(map(int, sys.stdin.readline().split()))
  run = lst[0:2]
  trick = lst[2:7]
  run_max = max(run)
  trick.sort(reverse=True)
  trick_sum = sum(trick[0:2])
  result = run_max + trick_sum
  result_lst.append(result)

print(max(result_lst))