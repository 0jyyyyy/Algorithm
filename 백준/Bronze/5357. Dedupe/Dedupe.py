n = int(input())

for _ in range(n):
    w = input()
    if not w: continue # 빈 문자열 예외 처리
    result = [w[0]] # 첫 글자는 무조건 포함
    
    for i in range(1, len(w)):
        # 현재 글자가 리스트의 마지막 글자와 다를 때만 추가
        if w[i] != result[-1]:
            result.append(w[i])
            
    print("".join(result))