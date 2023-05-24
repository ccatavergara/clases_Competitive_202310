from sys import stdin
# import io

# stdin = io.StringIO("""2
# ADAM
# MADAM
# """)

def advances_palindrome(counter, reverse, pali, word, length):
    tally = word.count(pali)
    if tally == 0:
        if counter < len(letters)-2:
            counter += 1
            palindrome_counter(counter,reverse, word)
        if counter == len(letters):
            print(length)
    if tally == 1:
        length2 = len(pali)
        if length2 > length:
            length = length2
            counter += 1
            if counter < len(reverse) - 1:
                pali += reverse[counter+1]
                advances_palindrome(counter, reverse, pali, word, length)
            else:
                print(length)
        else:
            print(length)

def palindrome_counter(counter,reverse, word):
    pali = reverse[counter:counter+2]
    pali = ''.join(pali)
    length = 0
    advances_palindrome(counter, reverse, pali, word, length)

cases = int(stdin.readline())

for x in range(cases):
    word = stdin.readline()

    length = 0
    letters = [*word]
    reverse = letters[:-1]
    reverse.reverse()
    counter = 0
    palindrome_counter(counter, reverse, word)