n = int(input())

for i in range(n):
    word = input()
    if len(word) > 9 or len(word) < 6:
        print('no')
    else:
        print('yes')