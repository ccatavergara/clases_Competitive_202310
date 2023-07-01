# from sys import stdin
import math
import io

stdin = io.StringIO("""6 12
5 141
6 142
0 0
""")

def find_prime_factors(num):
    factors = []
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1

    return factors

def repeat(num, dif):
    for x in range(1000):
        # print(num*x)
        if num * x == dif:
            return x
        if num * x > dif:
            return -1

def find_prime(prime_list, dif):
    times = -1
    for x in prime_list:
        if x != 0:
            times = repeat(x,dif)
            if times > -1:
                return times
    return times

lines = stdin.readlines()
lines.pop(-1)

for x, line in enumerate(lines):
    s,t = map(int, line.split())
    dif = t-s
    primes = find_prime_factors(s)
    print(primes)
    primes.reverse()

    times = find_prime(primes, dif)

    print(f'Case {x}: {times}')

