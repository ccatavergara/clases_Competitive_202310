# from sys import stdin
import math
import io

stdin = io.StringIO("""(*a++(*)
(*a{+}*)
""")

lines = stdin.readlines()

characters = '()[]{}<>!?*'
characters = [x for x in characters]
characters.append('(*')
characters.append('*)')

for line in lines:
    line = [x for x in line]
    original = line
    for x in line:
        if x not in characters:
            line.remove(x)
    print(line)
