import json
from termcolor import colored
from utils import parse_dict, parse_list

def read():
    words = dict()
    with open("words.json", 'r') as f:
        words = json.load(f)
        f.close()
        
    print(f"You have {len(words.keys())} unique words")

    try:
        nr = open("Not Remember", 'r')
        nrList = nr.read().strip().split("\n")
        print(f"{'*'*40}")
        print(f"{' '*10}{colored('Priority Words'.upper(), 'yellow')}\n")
        j = 0
        for i in nrList:
            if j <= 5:
                j += 1
                print(f"{colored(i, 'cyan')}", end=" "*2)
            else:
                j = 0
                print()
        print(f"\n{'*'*40}\n")
    except:
        pass

    input()

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


if __name__ == "__main__":
    read()
