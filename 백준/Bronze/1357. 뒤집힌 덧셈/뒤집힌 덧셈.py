x,y = map(int,input().split())

rev_x = str(x)[::-1]
rev_y = str(y)[::-1]

rev_sum = str(int(rev_x)+int(rev_y))[::-1]

print(int(rev_sum))