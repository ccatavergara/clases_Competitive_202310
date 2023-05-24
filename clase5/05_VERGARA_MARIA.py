#Etruscan warriors never play chess
import sys 
stdin = sys.stdin

cases = int(stdin.readline())
final_rows = []

for case in range(cases):
    warriors = int(stdin.readline())
    
    rows = 0 #there are no rows formed
    warriors_total = 0 #no warriors added
    
    while warriors >= warriors_total: #while the warriors are more than the counted for
        rows += 1 
        warriors_total += rows #this allows to know how many fit in total by counting the rows. 
    print(rows-1)
    
