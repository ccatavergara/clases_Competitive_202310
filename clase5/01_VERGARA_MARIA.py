from sys import stdin
# import io

# stdin = io.StringIO("""contest
# UFRN
# """)

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def prime(total):
    for i in primes:
        if (total % i) == 0: #this is if a number is divisible by 2 or any other number.
            return False
    return True    

words = (stdin.readlines())
for word in words:
    letters = [x for x in word]
    letters = letters[:-1]
    total = 0
    for letter in letters:
        total += (chars.index(letter) + 1)

    if total == 1:
        print('It is a prime word.')
    elif prime(total):
        print('It is a prime word.')
    else:
        print("It is not a prime word.")
    
        
    