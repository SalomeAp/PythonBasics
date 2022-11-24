"""
# H/W: Problem-solving (amazon):
# write a functions that return letters with counts, i.e. how many times each letter is used in the string (word, sentence, bigger text ..)
# Sample Input and Output: 'hello' -> {'h':1, 'e':1, 'l':2, 'o':1}
# album['letter'] += tracks  # adding the value to a previous value of the key in the dictionary
# album['letter'] = album['letter'] + tracks
"""


def occurrences(word):
    dict = {}
    for n in word:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(occurrences('Surreal'))
