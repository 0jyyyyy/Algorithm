import sys

n,m = map(int,sys.stdin.readline().split())
result = [0] * (n + 1)
for _ in range(m):
    k, s, e = map(int, sys.stdin.readline().split())
    
    # 현재 신청한 시작 시간(s)이 해당 강의실의 마지막 종료 시간보다 크거나 같은지 확인
    if s >= result[k]:
        print("YES")
        # 예약 성공 시 종료 시간 업데이트
        result[k] = e
    else:
        print("NO")