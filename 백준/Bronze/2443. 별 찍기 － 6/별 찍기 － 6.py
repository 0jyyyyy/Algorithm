n = int(input())
emp = 1
blank = 0
for i in range(n):
    print((" " * blank)+"*"*((2*n)-emp))
    emp += 2
    blank += 1