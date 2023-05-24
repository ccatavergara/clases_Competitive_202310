#Bangla Numbers
import sys 
stdin = sys.stdin

kuti = 10000000
lakh = 100000
hajar = 1000
shata = 100
counter = 1

def numbers(line):
    output = ''
    if (line % shata) < shata:
        output = f'{line % shata}'
    if (line // shata) >= 1: 
        output = f'{(line % hajar) // shata} shata ' + output
    if (line // hajar) >= 1:
        output = f'{(line % lakh) // hajar} hajar ' + output
    if (line // lakh) >= 1:
        output = f'{(line % kuti) // lakh} lakh ' + output
    #the whole division bigger than one means that it belongs to that category.    
        
    if (line // kuti) >= 1:
        output = f' kuti ' + output
        output_r = numbers(line//kuti) #creates a cycle in case the number is bigger
        output = output_r + output
        
    return output

while True:
    try:
        line = int(stdin.readline())
    except:
        break
    output = numbers(line)
    print(f' {counter}. {output}')
    counter += 1