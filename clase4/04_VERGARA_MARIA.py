# DNA

import sys 
stdin = sys.stdin

cases = int(stdin.readline())

def verify(dna, n, k): #this allows to know if the conditions that were set in the beggining are being followed
    return (len(dna) == n) and (n <= 10) and (k <= 5)

def change(output, cycle, dna_change):
    elements = ['a','g','c','t'] #this are the elements that compose the dna
    for x in range(len(elements)):
        dna_change[cycle] = elements[x] #this allows a letter of the dna to change for another of the elements in the list, it will always repeat 4 times.
        if ''.join(dna_change) not in output: 
            output.append(''.join(dna_change)) #this adds the new created dna to the final list.
    return output, (cycle + 1) #returns the final list, and changes the index of the dna so that it can change the iteration

def select(output, x, dna):
    cycle = 0
    for i in range(len(dna)):
        dna_change = [x for x in output[x]] #this allows to choose the dna we are changing from the list and it will go through every letter.
        output, cycle = change(output, cycle, dna_change)
    return output

def replace(dna, k, n):
    output = [''.join(dna)] #adds the original dna to the list
    if verify(dna, n, k): #makes sure the parameters work
        output = select(output, 0, dna) #goes though the first round of mutation
        if k > 1:
            k_counter = 1
            while k_counter < k: #this makes it go through the next rounds of mutation if there is more than one
                index = 1
                for x in range(1, len(output)):
                    output = select(output, index, dna)
                    index+=1
                k_counter += 1
                
                    
        
    output_sorted = sorted(output)
    print(len(output))
    for out in output_sorted:
        print(out.upper())
        
for case in range(cases):
    n, k = map(int, stdin.readline().split())
    dna = [x.lower() for x in stdin.readline()]
    dna = dna[:-1] #the dna list has an extra /n
    
    replace(dna, k, n)
    
"""
To try out, put this input by hand or add the # symbol so it also works when you copy and paste :

4
1 1
G
2 1
GA
2 1
AC
3 2
TCC
#  
"""