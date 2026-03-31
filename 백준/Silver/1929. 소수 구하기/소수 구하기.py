m, n = map(int, input().split())

# 0부터 n까지 모두 소수(True)라고 일단 표시함
prime_list = [True] * (n + 1)
prime_list[0] = prime_list[1] = False  # 0과 1은 소수가 아님

# 2부터 n의 제곱근까지만 확인
for i in range(2, int(n**0.5) + 1):
    if prime_list[i]:  # i가 소수라면
        # i의 배수들을 몽땅 False로 바꿈 (지워버림)
        for j in range(i * i, n + 1, i):
            prime_list[j] = False

# 이제 m부터 n까지 True로 남아있는 숫자만 출력
for i in range(m, n + 1):
    if prime_list[i]:
        print(i)