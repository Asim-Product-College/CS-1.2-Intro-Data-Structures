# if im importing another file that imports those modules, do i need to import
# them again here? - asssimung this'll werk!
from read_words import *

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

# im creating a new histogram for this, should i just do it inline?
# will i need to remember my old original histogram with the word counts?
def crea_histo_weights(histogram):
    '''
        Args:
            histogram: The histogram dictionary to generate from..
        Returns:
            histogram_weights: histogram dictionary with key(word) values(wieghts/percentages) from the dictionary.
    '''
    histogram_weights={}
    total = sum(histogram.values())
    
    for i in histogram: # for every word in histo(unique word, counts)
        weight = (histogram[i] / total) * 100
    #    print("i:", i,"val:", histogram.get(i) ,"wieght:", str(weight) + "%")
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
def gen_rand_word_from_frequency(histogram_weights):
    # zip the wieghts into 2 lists
        
    
# create_random_sentence
# call the function above 8 times.

# def test_randomness(random_word):
    words = source_text_to_list('/usr/share/dict/words')
    histogram = create_histogram(words)
    random_word = generate_random_word(histogram)
    for _ in 10000:
        words.append(generate_random_word(histogram))
        trueData = wordFrequency.create_histogram()
        data = normalize(wordFrequency.histogram(words), trueData, 10000)

if __name__ == '__main__':
    source_text = convert_textfile_to_list('book.txt')
    # words = source_text_to_list('histo_words.txt')
    histogram = create_histogram(source_text)
    print(histogram)
    histogram_weights = crea_histo_weights(histogram)
    random_word = generate_random_word(histogram_weights)
    # print(histogram_weights)
    print(random_word)