from termcolor import colored
from utils import parse_dict
import json

def search():
    with open("words.json", 'r') as f:
        words = json.load(f)
        f.close()
    
    print("Words Available\n-------------------------------\n")
    wordList = list(words.keys())
    j = 0
    for i in wordList:
        if j < 10:
            print(colored(i.capitalize(), 'cyan'), end=', ')
            j += 1
        else:
            print("\n")
            j = 0
    print(f"{len(wordList)} words in total")
    print("\n")

    while True:
        word = input("Search word: ").upper()
        if word.upper() == 'N':
            return
        if word in words.keys():
            print("Heres the meaning: ")
            print("\n=============================\n")
            print(colored(word, 'green'))
            parse_dict(len(word), None, words[word])
            print("\n=============================\n")
        
        else:
            print(f"{colored('We dont have this word, !!! sorry', 'red')} \N{disappointed face}")
        
        if input("Would you like to search more ?(Y/N)").upper() == 'N':
            break 
    
    return
        