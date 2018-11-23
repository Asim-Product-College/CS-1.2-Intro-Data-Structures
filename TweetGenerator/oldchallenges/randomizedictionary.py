'''Displays a random psuedo-sentence from user input of word count'''
import random
import sys

def get_dictionary():
    '''Creates a list of words.
        Args: None.
        Returns:
        A list of words from the OSX dictionary.
    '''
    with open("/usr/share/dict/words", 'r') as file:
        lst_words_in_dict = file.read().splitlines()
    return lst_words_in_dict

def create_random_sentence(dictionary, num_words):
    '''Creates a psuedo-sentence.
    Args:
        dictionary: A list of words from which the sentence will
            be constructed.
        num_words: An int of the number of words in the sentence.
    Returns:
        A "sentence" from words in dictionary with num_words
        number of words represented as a string.
    '''
    # random_array = list()
    for _ in range(num_words):
        return ' '.join(random.choice(dictionary) for _ in range(num_words))
        # random_array.append(rand_index)

if __name__ == "__main__":
    '''Tests get_dictionary() and create_random_sentence().'''
    print("Welcome to my Random Dictionary Values program...")
    num_words = int(input("How many words would you like to randomize: "))
    print(create_random_sentence(get_dictionary(), num_words))