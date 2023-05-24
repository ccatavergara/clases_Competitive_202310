from sys import stdin
# import io

# stdin = io.StringIO("""3
# 3
#     -1
#     6
# 10
#     4
#     -5
#     4
#     -3
#     4
#     4
#     -4
#     4
#     -5
# 4
#     -2
#     -3
#     -4""")

cases = int(stdin.readline())

for x in range(cases):
    stops = int(stdin.readline())
    start_aux = 1
    start = end = suma = ans = 0

    for i in range(2, stops+1):
        rating = int(stdin.readline())
        suma += rating
        if suma >= ans:
            if suma > ans or (suma == ans and (i - start_aux > end - start)):
                start = start_aux
                end = i
            ans = suma
        if suma < 0: #you have to start again if its negative.
            suma = 0
            start_aux = i
            
    if ans > 0:
        print(f"The nicest part of route {cases} is between stops {start} and {end}")
    else:
        print(f"Route {cases} has no nice parts")
