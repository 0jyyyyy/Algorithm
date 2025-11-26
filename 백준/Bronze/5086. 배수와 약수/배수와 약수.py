n_list = []
while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break 
    for i in range(1,n+1):
        if m % i == 0:
            n_list.append(i)
            if i != m//i:
                n_list.append(m //i)
            
    n_list = sorted(set(n_list))
    # print(n_list)

    if m % n ==0:
        print('factor')
    elif n % m ==0:
        print('multiple')    
    else:
        print('neither')