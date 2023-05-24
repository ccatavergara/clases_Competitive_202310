# from sys import stdin
import io

stdin = io.StringIO("""1
                    2
                    3
                    4
                    5
                    6""")

coins = [50, 25, 10, 5, 1]

#It is easier and consumes less memory to create a list with all the possibilities
equivalent = [0 for x in range(7490)]
equivalent[0] = 1  # not taking any coins also an option

for x in range(len(coins)):
    for i in range(1, len(equivalent)):
        if i >= coins[x]:
            equivalent[i] += equivalent[i-coins[x]] 
            
lines = stdin.readlines()

for line in lines:
    print(equivalent[int(line)]) #the answer, which was previously build in the list is by getting the value in the position of the amount requested.