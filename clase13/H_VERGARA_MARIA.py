from sys import stdin
# import math
# import io

# stdin = io.StringIO("""texasam!Rice!baYlor!csdept!BayloR!dev!Rice!bresearch!bpoucher
# """)

def bounce(words_lower): # I find the indexes from where the bounce starts and ends.
    start_index = -1
    end_index = -1

    for i in range(len(words_lower)):
        start_word = words_lower[i]

        if start_word in words_lower[i+1:]:
            end_index = words_lower.index(start_word, i+1)
            bounce_section = words_lower[i:end_index+1]

            if bounce_section == bounce_section[::-1]:
                start_index = i
                break

    return start_index+1, end_index+1 #I eliminate from the second word of the bounce to the last word. In the example above would be csdept and BayloR

words = stdin.readline().split('!')
words_lower = [x.lower() for x in words] # it is easier to compare the words like this

start, end = bounce(words_lower)

del words[start:end] #this lets me eliminate that seccion from the list

print('!'.join(words))
