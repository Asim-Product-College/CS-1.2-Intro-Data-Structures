import sys, random, re

# def convert_textfile_to_list(textfile):
#     with open(textfile, "r") as file:
#         list_of_words = file.read().replace('\n\n',' ')
#     print("list_of_words:",list_of_words)
#     return list_of_words

def convert_textfile_to_list(textfile):
    ''' Opens a textfile to read and splits words into a big list and formats the words'''
    with open(textfile) as f:
        word_data = f.read()
    # list_of_words = word_data.split() #split 
    # still slightly confused by this, need to read into it more. [ ] *mark when completed
    list_of_words = re.split('[^A-Za-z]+', word_data.lower())
    # print(list_of_words)
    return list_of_words

def get_words_from(filePath):
    ''' Takes a file with words separated by \n and returns them in a list '''
    return open(filePath, 'r').read().split('\n')
