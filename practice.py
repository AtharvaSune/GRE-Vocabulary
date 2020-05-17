from termcolor import colored
import random
import json
from utils import parse_dict
import time

def get_questions(nq, max):
    a = []
    for i in range(nq):
        num = random.randrange(0, max)
        while num in a:
            num = random.randrange(0, max)
        a.append(num)
    
    return a

def meanings(words):
    meanings_dict = dict()
    for word in words:
        meanings_dict[word] = []
        for pos in words[word]["meaning"]:
            for meaning in words[word]["meaning"][pos]:
                meanings_dict[word].append(meaning)
    
    return meanings_dict

def make_choices(allMeanings, questionWord):
    choices = []
    allWords = list(allMeanings.keys())
    realAnswer = allWords.index(questionWord)
    choices.append(random.choice(allMeanings[questionWord]))
    realAnswerString = choices[0]
    trials = 0
    while realAnswerString[0] == '(' and trials < 3:
        choices[0] = random.choice(allMeanings[questionWord])
        realAnswerString = choices[0]
        trials += 1

    for i in range(3):
        fakeAnswer = random.randrange(0, len(allWords))
        while fakeAnswer == realAnswer:
            fakeAnswer = random.randrange(0, len(allWords))
        choices.append(random.choice(allMeanings[allWords[fakeAnswer]]))
    
    random.shuffle(choices)
    realAnswerIndex = choices.index(realAnswerString)
    return choices, realAnswerIndex

def practice():
    try:
        nr = open("Not Remember", 'r')
        nrList = nr.read().strip().split("\n")
        print("open in append mode", nrList)
        nr.close()
    except:
        nr = open("Not Remember", "w+")
        nrList = list()
        nr.close()

    with open("words.json", "r") as f:
        words = json.load(f)
        f.close()

    wordsList = list(words.keys())
    meaning_dict = meanings(words)
    while True:
        nq = int(input("How many questions would you like to do?: "))
        print("In addition to this you will encounter questions you did wrong earlier.")
        print(f"Total number of questions: {nq + len(nrList)}\n")
        print("-"*41, end="\n\n")
        question_id = get_questions(nq, len(wordsList))
        questions = []
        for i in question_id:
            questions.append(wordsList[i])
        

        for i in nrList:
            if i not in wordsList:
                nrList.remove(i)
            elif i not in questions:
                questions.append(i)

        random.shuffle(questions)
        
        correctAnswers = 0
        wrongQuestions = []
        print(questions)
        for i, question in enumerate(questions):
            print("\n=============================\n")

            print(f"Q{i+1}/{len(questions)}. What is the meaning of {colored(question, 'blue')}")
            choices, realAnswerIndex = make_choices(meaning_dict, question)
            for j, val in enumerate(choices):
                print(f"{colored(str(j+1), 'cyan')}.{val}")
            
            print("\nEnter choice number: ", end='')
            answer = int(input())

            if answer == realAnswerIndex+1:
                print(f"{colored('Bingo!!!', 'green')}\N{grinning face}")
                if question in nrList:
                    nrList.remove(question)
                correctAnswers += 1

            else:
                print(f"{colored('Wrong Answer', 'red')}\N{disappointed face}")
                print(f"Correct answer is {colored(choices[realAnswerIndex], 'green')}")
                wrongQuestions.append(question)
                if question not in nrList:
                    nrList.append(question)
                
            print(f"Other meanings of {colored(question, 'green')} are")
            parse_dict(0, None, words[question]["meaning"])

            print("\n=============================\n")
            time.sleep(3)            

        print(f"======================== {colored('Report', 'blue') }=====================")
        print(f"""Number of correct questions: {correctAnswers}\nAccuracy: {(correctAnswers/len(questions))*100}%""")
        print(f"You got {len(wrongQuestions)} words wrong")
        for wq in wrongQuestions:
            print("\n=========================\n")
            print(colored(wq, 'green'))
            parse_dict(len(wq), None, words[wq]["meaning"])
            print("\n=========================\n")

        if input("Practice More (Y/N)?: ").upper() == 'N':
            nr = open("Not Remember", "w+")
            for i in nrList:
                nr.write(i)
                nr.write("\n")
            nr.close()
            break
    
    return
    


if __name__ == "__main__":
    practice()