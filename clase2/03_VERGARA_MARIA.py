import sys

stdin = sys.stdin
cases = int(stdin.readline())

for case in range(cases):
    enter = stdin.readline()
    if enter == '\n':
        keys = [int(x) for x in stdin.readline().split()]
        values = [float(x) for x in stdin.readline().split()]

        A = dict()
        for key in keys:
            if key not in A:
                A[key] = values[keys.index(key)]
        
        print()
        for x in range(len(keys)):
            print(A[x+1]) #this will show the results before allowing you to enter the second input. To enter the second input, you have to press enter and write the numbers.
