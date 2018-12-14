'''
    Histogram by Asim Zaidi - this program tell us the following:
    What is the least/most frequent word(s)?
    How many different words are used?
    What is the average (mean/median/mode) frequency of words in the text?

    Generates a histogram based on data structures to show frequency of words.
    (This is a preamble to a tweet generator assignment for CS 1.2)
'''

import sys
import timer
from read_words import convert_textfile_to_list

def histogram__d(source_text):
    '''
    Histogram function should take source_text as input (text file). - I already convert this to a list 
    This function returns a dictionary with every word in array(source_text)
    '''
    list_of_words = convert_textfile_to_list(source_text)
    histogram_dict = {}
    for word in list_of_words:
        if word not in histogram_dict:
            histogram_dict[word] = 1
        else:
            histogram_dict[word] += 1
    # how to find the highest key value in a dictionary - (How to get multiple highest values..?)
    # how to calcualte the lowest value in a dictionary
    # how to calcualte the different amount of words being used in this dictionary
    # tf how can i get avg mean median Dx
    highest_key = 0
    highest_val = 0
    for key, val in histogram_dict.items():
        if val > highest_val:
            highest_value = val
            highest_key = key



    print("The most frequent word appeared in our dictionary is:", highest_key , "at index", highest_val)

    return histogram_dict

def unique_words__d(histogram_dict):
    '''
    Count every work in histogram_dict and if any values equal 0, sum of unique words adds 1.
    '''
    unique_word_count = 0
    for key in histogram_dict:
        if histogram_dict[key] == 1:
            unique_word_count+=1
    return unique_word_count

def frequency__d(word, histogram_dict):
    '''
    takes a word and histogram argument and returns the number of times that word appears in a text.
    '''
    frequency_count = 0
    for key,val in histogram_dict.items():
        if word == key:
            frequency_count = val
    return frequency_count

def histogram__lol(source_text):
    '''
    Args:
        text: The string to generate from.
    Returns:
        A list of lists in the format [[word, occurences], ...].
    '''
    list_of_words = convert_textfile_to_list(source_text)
    histogram__lol = []
    # checks each word in the source text
    for word in list_of_words:
        # create this inner list, jaa feel me!
        count_and_word = []
        word_count = list_of_words.count(word)
        count_and_word.append(word) #i don't think the order of thse dawgs matter THO.
        count_and_word.append(word_count)
        # counts up the words in the source text and adds count and word to list
        if count_and_word not in histogram__lol:
            histogram__lol.append(count_and_word)
        else:
            pass
        # i think this will create a list within our list with these values
        # histogram_list.extend([word,word_count])
    return histogram__lol

def unique_words__lol(histogram_lol):
    '''
    Count every work in histogram_lol and if any values equal 0, sum of unique words adds 1.
    '''
    unique_word_count = 0
    for lst in histogram_lol:
        if lst[1] == 1:
            unique_word_count+=1
    return unique_word_count

def frequency__lol(word, histogram_lol):
    '''
    takes a word and histogram argument and returns the number of times that word appears in a text.
    '''
    frequency_count = 0
    for lst in histogram_lol:
        if lst[0] == word:
            frequency_count = lst[1]
    return frequency_count

def histogram__lot(source_text):
    '''
    Args:
        text: The string to generate from.
    Returns:
        A list of tuples in the format [(word, occurences), ...].
    '''
    list_of_words = convert_textfile_to_list(source_text)
    histogram = []
    for word in list_of_words:
        h_tuple = (word, list_of_words.count(word))
        if h_tuple not in histogram:
            histogram.append(h_tuple)
        else:
            pass
    return histogram

def unique_words__lot(histogram_lot):
    '''
    Count every word in histogram_lot and if any values equal 0, sum of unique words adds 1.
    '''
    unique_word_count = 0
    for tpl in histogram_lot:
        if tpl[0] == 1:
            unique_word_count+=1
    return unique_word_count

def frequency__lot(word, histogram_lot):
    '''
    takes a word and histogram argument and returns the number of times that word appears in a text.
    '''
    frequency_count = 0
    for tpl in histogram_lot:
        if tpl[0] == word:
            frequency_count = tpl[1]
    return frequency_count

# def histogram__loc(source_text):
    #     '''
    #     Args:
    #         text: The string to generate from.
    #     Returns:
    #         A list of tuples in the format [(word, occurences), ...].
    #     '''
    #     list_of_words = convert_textfile_to_list(source_text)
    #     histogram = []
    #     for word in list_of_words:
    #         h_tuple = (word, list_of_words.count(word))
    #         if h_tuple not in histogram:
    #             histogram.append(h_tuple)
    #         else:
    #             pass
    #     return histogram
# def unique_words__loc(histogram_loc):
    #     '''
    #     Count every word in histogram_lot and if any values equal 0, sum of unique words adds 1.
    #     '''
    #     unique_word_count = 0
    #     for tpl in histogram_loc:
    #         if tpl[0] == 1:
    #             unique_word_count+=1
    #     return unique_word_count
# def frequency__loc(word, histogram_loc):
    #     '''
    #     takes a word and histogram argument and returns the number of times that word appears in a text.
    #     '''
    #     frequency_count = 0
    #     for tpl in histogram_loc:
    #         if tpl[0] == word:
    #             frequency_count = tpl[1]
    #     return frequency_count
# def use_loc_method():
    #     histogram_loc = histogram__loc('histo_words.txt')
    #     print("Histogram List of Counts: ", histogram_loc)
    #     unique_word_count = unique_words__lot(histogram_loc)
    #     print("Unique Word Count: ", unique_word_count)
    #     user_guessed_word = input("Guess a word in the histogram and I'll tell you how many times it occurs! \nEnter Word: ")
    #     frequency_count = frequency__loc(user_guessed_word, histogram_loc)
    #     print(user_guessed_word,"occurs",frequency_count,"times.")

def use_dictionary_method():
    '''
    // create var that uses imported functions that takes txt file and turns it into array of words.
    // source_text = read_in_txtfile('histo_words.txt')
    // pass in source text to histogram function to run it.
    '''
    histogram_dict = histogram__d('histo_words.txt')
    print("Histogram Dictionary: ", histogram_dict)
    unique_word_count = unique_words__d(histogram_dict)
    print("Unique Word Count: ", unique_word_count)
    user_guessed_word = input("Guess a word in the histogram and I'll tell you how many times it occurs! \nEnter Word: ")
    frequency_count = frequency__d(user_guessed_word, histogram_dict)
    print(user_guessed_word,"occurs",frequency_count,"times.")

def use_lol_method():
    histogram_lol = histogram__lol('histo_words.txt')
    print("Histogram List of Lists: ", histogram_lol)
    unique_word_count = unique_words__lol(histogram_lol)
    print("Unique Word Count: ", unique_word_count)
    user_guessed_word = input("Guess a word in the histogram and I'll tell you how many times it occurs! \nEnter Word: ")
    frequency_count = frequency__lol(user_guessed_word, histogram_lol)
    print(user_guessed_word,"occurs",frequency_count,"times.")

def use_lot_method():
    histogram_lot = histogram__lot('histo_words.txt')
    print("Histogram List of Tuples: ", histogram_lot)
    unique_word_count = unique_words__lot(histogram_lot)
    print("Unique Word Count: ", unique_word_count)
    user_guessed_word = input("Guess a word in the histogram and I'll tell you how many times it occurs! \nEnter Word: ")
    frequency_count = frequency__lot(user_guessed_word, histogram_lot)
    print(user_guessed_word,"occurs",frequency_count,"times.")

def prompt_user_choice():
    ''' Get user choice for what data structure they'd like to use.'''
    print("Would you like to use a dictionary or lists or lists?")
    choice = input("Select\nA: Dictionary\nB: List of Lists\nC: List of Tuples\nD: List of Counts\n")
    if choice == "a" or choice == "A":
        use_dictionary_method()
    elif choice == "b" or choice == "B":
        use_lol_method()
    elif choice == "c" or choice == "C":
        use_lot_method()
    elif choice == "d" or choice == "D":
        use_loc_method()

if __name__ == '__main__':
    prompt_user_choice()

