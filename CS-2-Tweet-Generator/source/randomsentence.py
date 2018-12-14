'''
    Created by: Asim Zaidi
    https://www.asimzaidi.tech
    https://www.github.com/awesomezaidi

    • This program can create a histogram(dictionary) or words with their occurances from a 
        text file.
    • Finds their weighted values (percentage they occur) in a new histogram.
    • Generates a random sentence based off of word frequencies.
'''
from file_methods import *

def create_histogram(words):
    '''
        Args:
            words: list of strings(words).
        Returns:
            A dictionary in the format {word : occurance, ...}.
    '''
    histogram = {}
    # how to use a for loop list comprehension here? - #TODO: Ask Ikey.
    for word in words[:100]:
        if word not in histogram: 
            histogram[word] = 1  
        else:
            histogram[word] += 1
    return histogram

def create_histo_weights(histogram):
    '''
        Args:
            histogram: The histogram dictionary to generate from.
        Returns:
            histogram_weights: histogram dictionary with key(word) values(wieghts/percentages) from the dictionary.
    '''
    histogram_weights={}
    total = sum(histogram.values())
    
    for i in histogram:
        weight = (histogram[i] / total) * 100
        histogram_weights[i] = weight
    
    return histogram_weights

def generate_random_word(histogram_weights):
    '''
        Args:
            histogram_wights: The histogram dictionary with weights to generate from.
        Returns:
            random_key: random key word from the dictionary
    '''
    return random.choice(list(histogram_weights))
    # pull random word (call function) to prove how random it is...

def test_randomness(random_word):
    # words = source_text_to_list('/usr/share/dict/words')
    # histogram = create_histogram(words)
    # random_word = generate_random_word(histogram)
    # for _ in 10000:
    #     words.append(generate_random_word(histogram))
    #     trueData = wordFrequency.create_histogram()
    #     data = normalize(wordFrequency.histogram(words), trueData, 10000)
    pass

def main():
    source_text = convert_textfile_to_list('book.txt')
    # words = source_text_to_list('histo_words.txt')
    histogram = create_histogram(source_text)
    sentence = random_sentence(histogram)

    print(sentence)


main()