from sys import stdin
# import io

# stdin = io.StringIO("""2
# 3 2
# 1 2
# 2 3
# 10 12
# 1 2
# 3 1
# 3 4
# 5 4
# 3 5
# 4 6
# 5 2
# 2 1
# 7 1
# 1 2
# 9 10
# 8 9
# """)

cases = int(stdin.readline())

def merging(friends):
    final = []
    while len(friends) > 0:
        common = set(friends[0])
        i = 1
        while i < len(friends):
            if common.intersection(friends[i]): #this adds all the the friends that can be found paired with "common"
                common.update(friends[i]) #it goes to the next person in the line
                friends.pop(i) 
            else:
                i += 1
        final.append(list(common)) #it adds the friends list.
        friends.pop(0)
    return final

for x in range(cases):
    total_people, pairs = map(int, stdin.readline().split()) #this divides how many people there are and the total friends pairs
    friends = []
    for i in range(pairs):
        lista = [int(x) for x in stdin.readline().split()]
        lista.sort() #this adds each friend pair as a list to a bigger list
        friends.append(lista)

    friends.sort()
    final = merging(friends) #this merges the friends lists

    final2 = merging(final) #this merges the already merged list in case the first merge did not work
    amount = 0
    for group in final2:
        if len(group) > amount:
            amount = len(group)
    print(amount) #prints the longest friend group.