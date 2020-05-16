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
            
            while cont.upper() != 'N':
                if cont == 'y':
                    wordList = input("Enter the word (if >1 space separated): ").split()
                else:
                    wordList = cont
                wordList = [i.upper() for i in wordList]

                for word in wordList:
                    if word in prev_words.keys():
                        print(f"You have encountered the word {word}")
                        print("Try and remember (10 seconds)")
                        wait = 'y'
                        r = False
                        while wait.upper()=='Y':
                            time.sleep(10)
                            if input("Remember ?: ").upper() == 'Y':
                                wait = 'n'
                                r = True
                            else:
                                if input("Continue waiting ?(10 seconds): ").upper() == 'Y':
                                    wait = 'y'
                                else:
                                    wait = 'n'
                        
                        if not r:
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
                            print(f"{colored('We dont have this word, !!! sorry', 'red')} \N{disappointed face}")
                            nf = open("Not Found", 'a+')
                            nf.write(word.upper())
                            nf.write("\n")
                            nf.close()

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
                                print(f"{colored('We found the word', 'green')} \N{grinning face}")

                cont = input("New word (if >1 space separated): ")
            
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

        
