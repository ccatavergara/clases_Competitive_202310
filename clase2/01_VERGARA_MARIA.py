import sys

stdin = sys.stdin
number = int(stdin.readline())

#https://github.com/morris821028/UVa/blob/master/volume111/11150%20-%20Cola.cpp

while number != 0:
    total = number
    while number >= 3:
        total += number//3
        number = (number//3 + number%3)
    if number == 2:
        total += 1
    print(total)
    number = int(stdin.readline())