# TweetGenerator

##Histogram Implementations

###DataStructure        Effort                          Speed               Memory

Dictionary              easy, less code, intuitive      Faster than lists O(1)                  
(key-value)              

Liste of Lists          easy                            Slowest             Least Efficient

List of Tuples          harder than lists of lists      Slower than dict    More efficient than
                        bc tuples are immutable         Faster than LoL     Lists of list
                                                                            Most Efficient

List of Counts                                          Fastest

##Word Freq

Tokens - offurences of words (Objects)
Types - Distinct words (Classes)

build  afunction like same by frequency
    - do some sort of sampling technique...
    sleect a word - get freq
    - create an unfair die and roll it to see what you get...
    

i programming theres data and functions that take parameters and return values.
data can refer to other data as well.

class - data declaration, function declarations

instances of the object create classes and each one has their own data and functions.

there's only one isntance of every function these things live insdie the class definiton.

swift compiles these things the exact same under the hood.

#Markov Chains

search best - gen random sentence. 
find one word use that to find another word, add that to the sentence.
use new word as search word to find a new word to add to the sentence 
and keep repeating this process like 8 times.
- The most basic markov chain.

one fish two fish red fish blue fish

 - fish is followed by two, red, blue.
 - this is the concept of a state diagram which is the basis of a markov model.
 - after two, we have fish, and that's a transition back from one state to another.
 - red goes to fish, blue goes to fish.
 - one goes to fish
 - states are word types
 - 

 word tokens that are after the word type fish.
 type fish
 --------
 two:  1
 red:  2
 blue: 1

a dictionary that maps a word to a histogram.
states are word types 

N-Gram - is a contiguous (order matters) sequence of items, which in this case is the words in text.
Out steps to generate a random sentence based on wieghts:
What we want to do is build up a dictionary of N-grams, which are pairs, triplets or more (the N) of words that pop up in the training data, ith the value being the number of times they showed up.