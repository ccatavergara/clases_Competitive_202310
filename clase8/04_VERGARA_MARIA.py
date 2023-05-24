from sys import stdin
# import io

# stdin = io.StringIO("""galore galore abase python python python chit seraphic reunite bruising chit chit lode tobago reunite chit whitby chit abase bruising whitby seraphic lode python seraphic abase seraphic tobago seraphic chit chit tobago lode galore galore seraphic chit lode lode unfashionable galore seraphic 
# #
# lode python seraphic whitby cowslip seraphic abase lode galore abase tobago reunite unfashionable 
# #
# conventual rotund laureate adulterous suzerainty antediluvian petiole conventual adulterous petiole rotund rotund crevasse hessian laureate suzerainty laureate conventual locus hessian salty unhindered suzerainty theorist unhindered conventual unhindered sluggard 
# #
# adulterous rotund rhea theorist salty rhea ensnare rhea scraggy ensnare ensnare humped petiole humped petiole locus ensnare crevasse scraggy ensnare laureate conventual flaccid salty mauritania antediluvian locus locus humped conventual crevasse abaft unhindered flaccid crevasse demerit ensnare laureate adulterous abaft ensnare unhindered adulterous ensnare laureate adulterous 
# #
# """)


def split_list(lines): #this function allows me to split by text when it finds a #
    result = []
    temp = []
    
    for line in lines:
        if line == "#\n":
            result.append(temp)
            temp = []
        else:
            temp.append(line)
    result.append(temp)
    
    return result


lines = stdin.readlines()

new_lines = split_list(lines[:-1])

for x in range(0,len(new_lines),2):
    sentences1 = new_lines[x]
    sentences2 = new_lines[x+1]
    print(sentences1,sentences2)

    words1 = []
    words2 = []

    for line in sentences1:
        words1.extend(line.split())
    for line in sentences2:
        words2.extend(line.split())

    final_list = []
    setlist = ''
    for word in words2:
        if word in words1 and word not in final_list:
            setlist += f'{word} '
            final_list.append(word)
    print(setlist)
