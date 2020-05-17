from write import write
from read import read
from search import search
from practice import practice
from termcolor import colored

def main():
    print("you have the following options: \n1. Write(w) \n2. Read(r) \n3. Search(s) \n4. Practice(p) \n5. Quit(q)")
    
    while True:
        job = input("What would you like to do: ").lower()
        if job == 'w' or job == '1':
            verbose = input("Want to display meaning of new words you search? (Y/N): ").upper()
            test = input("Giving a test/activity ? (Y/N): ").upper()
            if test == 'Y':
                test = True
            else:
                test = False
            write(verbose, test)

        elif job == 'r' or job == '2':
            read()

        elif job == 's' or job == '3':
            search()

        elif job == 'p' or job == '4':
            practice()
        
        elif job == 'q' or job == '5':
            print("Bye Bye See you again later \N{smiling face with open mouth}")
            exit(0)

if __name__ == "__main__":
    main()