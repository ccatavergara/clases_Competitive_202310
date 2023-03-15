
from sys import stdin
import io

stdin = io.StringIO("""UBQTS TXT
tthumb
LIVESPACE BLOGJAM
philton
aeinstein
YOUBOOK
j97lee
sswxyzy
j97lee
aeinstein
SKINUX
1
0""")

dic = {}
names_list = {}
order = {}
for line in stdin.readlines():
    if line != "1":

        if line.isupper() == True: #significa que es equipo
            name = line
            dic[line] = list()
        if line.islower() == True and line not in names_list: #significa que es usuario y que es primera vez que se ve su usuario
            names_list[line] = list()
            names_list[line].append(name)
            dic[name].append(line)
        elif line.islower() == True and line in names_list: #significa que es usuario pero ya ha aparecido su nombre
            if name not in names_list[line]: #aca si es que esta su nombre en mas de una lista
                names_list[line].append(name)
        
        for user in names_list:
            if len(names_list[user]) > 1: # si es que esta en mas de una lista
                for team in dic:
                    if user in dic[team]:
                        dic[team].remove(user) #el usuario se va a borrar de todas las listas en la que se inscribio
        
        for team in dic:
            order[team] = len(dic[team]) # aca esta viendo cuantos usuarios hay por lista
            new_order = sorted(order.items(), key=lambda x:x[1]) #esta ordenando tanto en orden alfabetico como de numero la lista.
            
        new_order.reverse() #se da vuelta la lista para que quede de mayor a menor.
        
for x in new_order:
    print(x[0].strip('\n'), x[1]) #imprime
