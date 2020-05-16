from PyDictionary import PyDictionary
import json
import time
import sys, os
from utils import parse_dict
from termcolor import colored

def write(verbose = 'N', test = True):
    words = dict()
    sys.stdout = open(os.devnull, 'w')
    dictionary = PyDictionary('features="html.parser"')
    sys.stdout = sys.__stdout__
    cont = 'y'
    try:
        with open("words.json", "r+") as f:
            try: 
                prev_words = json.load(f)
            except:
                prev_words = dict()
            
            while cont[0].upper() != 'N':
                if cont == 'y':
                    wordList = input("Enter the word (if >1 space separated): ").split()
                else:
                    wordList = cont
                wordList = [i.upper() for i in wordList]

                for word in wordList:
                    if word in prev_words.keys():
                        print(f"You have encountered the word {word}")
                        print("Try and remember")
                        
                        r = False
                        if not test:
                            wait = 'y'
                            while wait.upper()=='Y':
                                time.sleep(10)
                                if input("Remember ?: ").upper() == 'Y':
                                    wait = 'n'
                                    r = True
                        
                        if not r:
                            nr = open("Not Remember", "r+")
                            nrList = nr.read().strip().split("\n")
                            if word not in nrList:
                                nr.write(word.upper())
                                nr.write("\n")
                            nr.close()
                            del nr
                            del nrList
                            
                            if test:
                                print(f"{colored('Bad luck look it up later', 'cyan')} \N{disappointed face}")
                            else:
                                print("Heres the meaning: ")
                                print("\n=============================\n")
                                print(colored(word, 'green'))
                                parse_dict(len(word), None, words[word])
                                print("\n=============================\n")

                    else:

                        sys.stdout = open(os.devnull, 'w')
                        meaning = dictionary.meaning(word)
                        synonyms = dictionary.synonym(word)
                        antonyms = dictionary.antonym(word)
                        sys.stdout = sys.__stdout__

                        if meaning is None:
                            print(f"{colored(f'We dont have the word {word}, !!! sorry', 'red')} \N{disappointed face}")
                            nf = open("Not Found", 'a+')
                            nfList = set(nf.read().strip().split("\n"))
                            if word not in nfList:
                                nf.write(word.upper())
                                nf.write("\n")
                            nf.close()
                            del nf
                            del nfList

                        else:
                            words[word] = dict()
                            words[word]["meaning"] = meaning
                            words[word]["synonym"] = synonyms
                            words[word]["antonyms"] = antonyms

                            if verbose == 'Y':
                                print("Heres the meaning: ")
                                print("\n=============================\n")
                                print(colored(word, 'green'))
                                parse_dict(len(word), None, words[word])
                                print("\n=============================\n")
                            else:
                                print(f"{colored(f'We found the word {word}', 'green')} \N{grinning face}")

                cont = input("New word (if >1 space separated): ").split()
            
            prev_words.update(words)
            f.seek(0)
            
            try:
                json.dump(prev_words, f,indent=2, sort_keys=True)
                f.close()
            except:
                print("could not write to file")
                prev_words = json.dumps(prev_words, indent=2)
                print("Printing on console copy to the file")
                print("\n\n=========================================\n")
                print(prev_words)
                print("=========================================\n")
                f.close()

        
    except EnvironmentError as e:
        print(f"Something went wrong\n {e}")

    return

if __name__ == "__main__":
    v = input("Do you want to display meaning of words added?(Y/N): ").upper()
    test = input("Giving any test or activity(Y/N): ").upper()
    if test == 'Y':
        test = True
    else:
        test = False
    
    write(v, test)