from termcolor import colored
from utils import parse_dict
import json

def search():
    with open("words.json", 'r') as f:
        words = json.load(f)
        f.close()
    
    with open("Not Remember", 'r') as f:
        nrList = f.read().strip().split("\n")
        f.close()

    print("Words Available\n-------------------------------\n")
    wordList = list(words.keys())
    j = 0
    for i in wordList:
        if j < 10:
            if i.upper() in nrList:
                color = 'red'
            else:
                color = 'cyan'

            print(colored(i.capitalize(), color), end=', ')
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

if __name__ == "__main__":
    search()