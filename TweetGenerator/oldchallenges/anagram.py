import sys
import random
from itertools import permutations
import timeit

def anagram():
    # open dictionary file
    f = open('/usr/share/dict/words')
    # store words in file into list
    dictionary = list(f.read().splitlines())
    # ask user for a word input
    word = input("Enter a word and we'll find all the possible anagrams for it: ")
    # randomize all the possible computions of that string. Store all words into a list.
    perms = [''.join(p) for p in permutations(word)]
    # len(set(perms))

    # use hash map to read through dictionary in constant time
    counter=0
    anagram_words = []
    for i in dictionary:
        if i in perms:
            anagram_words.append(i)


    print(anagram_words)
anagram()

# t=timeit.timeit('mylist[99]',setup='mylist=list(range(100))',number=10000000)
# print (t)
# t=timeit.timeit('mylist[-1]',setup='mylist=list(range(100))',number=10000000)
# print (t)

# Learnings
# Lists are arrays (of pointers to elements)
