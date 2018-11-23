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

# function to generate random word based on frequency
def random_word(histogram):
    '''
        gen ran sent
          • dafa
    '''
    words, frequencies = zip(*histogram.items())
    # [red, blue, green]
    # [2,3,4,5]

    accumulator, accumulated = 0, []
    for i in frequencies:
        accumulator += i
        accumulated.append(accumulator)
    
    #[2,5,9,14]
    # print("accumulated:",accumulated)

    random_num = random.randint(0, accumulator)
    # loop thru each accum val, and enumerator - so u have its'n index
    for index, seperator in enumerate(accumulated):
        if random_num < seperator:
            return words[index]

def random_sentence(histogram):
    sentence = []
    for i in range(8):
        sentence.append(random_word(histogram))
    sentence = " ".join(sentence)
    return sentence

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