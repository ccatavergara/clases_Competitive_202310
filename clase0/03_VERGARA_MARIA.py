from sys import stdin
import io

stdin = io.StringIO("""1 2 3 4 5 6 7 8 9
5 10 5 20 10 5 10 20 10""")

for line in stdin.readlines():
    data = [int(x) for x in line.split()]
    b = [data[0], data[3], data[6]]
    g = [data[1], data[4], data[7]]
    c = [data[2], data[5], data[8]]
    
    combinations = ['bgc', 'bcg', 'gbc', 'gcb', 'cgb', 'cbg']
    
    #the list of all the combinations in the order of the list above.
    minimun = [(b[1] + b[2] + g[0] + g[2] + c[0] + c[1]),
    (b[1] + b[2] + g[0] + g[1] + c[0] + c[2]),
    (b[0] + b[2] + g[1] + g[2] + c[0] + c[1]),
    (b[0] + b[1] + g[1] + g[2] + c[0] + c[2]),
    (b[1] + b[0] + g[0] + g[2] + c[2] + c[1]),
    (b[0] + b[2] + g[0] + g[1] + c[2] + c[1])]
    


    print(combinations[minimun.index(min(minimun))].upper(), min(minimun))
    #to find the minimum number of changes, you use min and then find its index that determines which combination it is from the list above. This allows you to not write any loops and so simple list findings.