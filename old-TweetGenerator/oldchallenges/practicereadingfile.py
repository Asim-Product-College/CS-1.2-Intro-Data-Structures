import sys
import random

''' takes num from terminal and return num random words from dictionary of words converted into a list'''
def randomWords(num):
    f = open('/usr/share/dict/words')
    new_list = list(f.read().splitlines())
    end_of_list = len(new_list)-1
    for i in range(0,int(num)):
        print(new_list[random.randint(0,end_of_list)], end=' ')

def main():
    num = sys.argv[1]
    randomWords(num)

main()