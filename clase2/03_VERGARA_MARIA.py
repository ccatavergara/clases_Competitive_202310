# import sys

# stdin = sys.stdin
# cases = int(stdin.readline())


from sys import stdin
import io

stdin = io.StringIO("""1 10 5 2.0
1 5 10.0 2
2 10 11 2
3 5 1 6
4 5.0 -1 6
0""")
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
