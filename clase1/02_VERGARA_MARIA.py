
from sys import stdin
import io

stdin = io.StringIO("""4
XXXX                XXXXX
XXX               XXXXXXX
XXXXX                XXXX
XX                 XXXXXX
2
XXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXX
1
XXXXXXXXX              XX
0""")

cases = int(stdin.readline())

while cases != 0:
    filas = []
    blanks = 25
    new_blanks = 0
    for x in range(cases):
        filas.append(stdin.readline())
    for fila in filas:
        counts = fila.count(" ")
        if counts < blanks:
            blanks = counts
    for fila in filas:
        fila = fila.replace(' ', "", blanks)
        new_blanks += fila.count(" ")
    print(new_blanks)
    cases = int(stdin.readline())