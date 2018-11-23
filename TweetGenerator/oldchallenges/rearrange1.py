'''
    Module for rearranging the arguments pasased into this module for function

    randomize_args = Randomizes the output of the args passed into it
'''
import sys
import random
def randomize_args(args):
    '''
    Takes the argument and randomly selects which one to print
    Assumes args is a list with n items. Re
    '''
    original_list = len(args)
    arguments_switched = []
    # while len(args) > 0:
    #     random_num = random.randint(0,len(args)-1)
    #     arguments_switched.append(args.pop(random_num))
    for _ in range(original_list):
        random_num = random.randint(0,len(args)-1)
        arguments_switched.append(args.pop(random_num))
    print(" ".join(arguments_switched))
    
    return arguments_switched

if __name__ == '__main__':
    arguments = sys.argv[1:]
    print(randomize_args(arguments))