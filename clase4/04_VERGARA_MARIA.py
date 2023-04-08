import sys 
stdin = sys.stdin

cases = int(stdin.readline())
elements = ['a','g','c','t']



for case in range(cases):
    n, k = map(int, stdin.readline().split())
    dna = [x.lower() for x in stdin.readline()]
    print(dna)