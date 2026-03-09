n = int(input())

result = n

for _ in range(n):
    word = input()
    for i in range(len(word) - 1):
        # 현재 문자와 다음 문자가 다른데
        if word[i] != word[i+1]:
            # 다음 문자가 그 이후 문자열에 또 포함되어 있다면 그룹 단어가 아님
            if word[i] in word[i+1:]:
                result -= 1
                break
print(result)