min = sum(map(int, input().split()))

man = sum(map(int, input().split()))

# 둘 중 더 큰 점수를 출력 (같으면 그 점수 출력)
print(max(min, man))
