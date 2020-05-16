import json
from termcolor import colored
from utils import parse_dict, parse_list

def read():
    words = dict()
    with open("words.json", 'r') as f:
        words = json.load(f)
        f.close()
        
    print(f"You have {len(words.keys())} unique words")


    for key in words.keys():
        print("=========================================\n")
        
        print(colored(key, 'green'))
        parse_dict(len(key.strip()) , None, words[key])
        
        print("\n=========================================")
        waitKey = input()
        if waitKey == '':
            continue
        else:
            return
    
    print(colored("All Words Finished", 'yellow'))
