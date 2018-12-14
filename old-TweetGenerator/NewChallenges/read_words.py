import sys, random, re

#reads in from text file and saves to an list
def convert_textfile_to_list(textfile):
    with open(textfile) as f:
        word_data = f.read()
        # print("word_data:",word_data)
    # list_of_words = word_data.split() #split 
    # still slightly confused by this, need to read into it more. [ ] *mark when completed
    list_of_words = re.split('[^A-Za-z]+', word_data.lower())
    return list_of_words

def get_words_from(filePath="/usr/share/dict/words"):
    ''' Takes a file with words separated by \n and returns them in a list '''
    return open(filePath, 'r').read().split('\n')

#grabs the number user enters to specify # of words for sentence
# def get_word_count():
#     if len(sys.argv) == 1:
#         print("Error: no number entered.")
#     else:
#         count_string = str(sys.argv[1])
#         return int(count_string)

#generates and prints out random sentence string
# def print_random_sentence(word_bank, num_of_words):
#     rand_sentence_string = ""
#     for index in range(0, num_of_words):
#         rand_item = word_bank.pop(random.randint(0, len(word_bank) - 1))
#         rand_sentence_string = rand_sentence_string + " " + rand_item
#     print(rand_sentence_string)


# if __name__ == '__main__':
#     start = time.time()
#     print_random_sentence(read_in_txtfile('word.txt'),get_word_count())
#     end = time.time()
#     print(end - start)