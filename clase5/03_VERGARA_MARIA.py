#498 bits
import sys 
stdin = sys.stdin


while True:
    try:
        x = int(stdin.readline())
    except:
        break
    a_list = [int(i) for i in stdin.readline().split()]
    
    total = 0
    n = len(a_list)
    for i in range(len(a_list)):
        if n-1-i == 0:
            total += a_list[i]*(n-i-1)*(x**(0))
        else:
            total += a_list[i]*(n-i-1)*(x**(n-2-i))
    print(total)