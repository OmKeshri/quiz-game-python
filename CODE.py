# Modules Import
import random
import time
from pygame import mixer

# Function
def quiz_game():
    points = 0
    right_answers = {}
    your_answers = {}
    questions = {"Mount Kilimanjaro is the world's tallest peak.": "FALSE",
                 "The longest river in the world is Amazon River.": "FALSE",
                 "The capital of Morocco is Marrakesh.": "TRUE",
                 "In a regular deck of cards, all kings have a mustache.": "FALSE",
                 "When the two numbers on opposite sides of a dice are added together,"
                 " it always equals 7.": "TRUE",
                 "Google was initially called BackRub.": "TRUE",
                 "Harry Potter's first flying stick name is Firebolt.": "FALSE",
                 "It is possible to sneeze while sleeping.": "FALSE",
                 "The national flag of America has 51 stars.": "TRUE",
                 "The horn of Rhinoceros is made of hairs.": "TRUE",
                 "The black box in a plane is black.": "FALSE",
                 "Monaco is the smallest country in the world.": "FALSE",
                 "Fish cannot blink.": "TRUE",
                 "Goldfish have a two second memory.": "FALSE",
                 "There are 14 bones in a human foot.": "FALSE",
                 "The liver is the largest internal organ in the human body.": "TRUE",
                 "The human eyes can observe 10 million different colors.": "TRUE",
                 "The average human body consists of 60% water.": "TRUE"}

    for i in range(1, 6):
        print("\nROUND %d" % i)
        mixer.music.load("Sounds\\round%s.mp3" % i)
        mixer.music.play()
        time.sleep(1)
        for j in range(1, 3):
            ques = random.choice(list(questions.keys()))
            print("\nQues%d: %s" % (j, ques))
            right_answers[ques] = questions[ques]
            mixer.music.load("Sounds\\question%d.mp3" % j)
            mixer.music.play()
            time.sleep(1)

            mixer.music.load("Sounds\\%s.mp3" % ques)
            mixer.music.play()

            ans = input("Ans: ")
            if len(ans) == 0:
                while len(ans) == 0:
                    print("Please write the answer!")
                    mixer.music.load("Sounds\\please write the answer..mp3")
                    mixer.music.play()
                    time.sleep(1)
                    ans = input("Ans: ")
            else:
                ans = ans.upper()
                your_answers[ques] = ans

            if ans == questions[ques]:
                points += 1
                print("Congratulation! You gave the right answer.")
                mixer.music.load("Sounds\\congrats.mp3")
                mixer.music.play()
                time.sleep(2.4)
            else:
                print("Sorry! You gave the wrong answer.")
                mixer.music.load("Sounds\\sorry.mp3")
                mixer.music.play()
                time.sleep(2.1)
                pass

            questions.pop(ques)

    print("\nTHANK YOU FOR PLAYING THIS GAME!")
    mixer.music.load("Sounds\\Thankyou.mp3")
    mixer.music.play()
    time.sleep(3.2)
    print("YOUR POINTS:", points)
    print("\nRIGHT ANSWERS:", right_answers)
    print("Your ANSWERS: ", your_answers)

    print("\nDEVELOPERS NAME:- OM KESHRI")


mixer.init()

print("WELCOME TO THE QUIZ GAME!")
# mixer.music.load("Welcome to the Quiz Game.mp3")
mixer.music.load("Sounds\\Welcome to the Quiz Game.mp3")
mixer.music.play()
time.sleep(1.8)

print("PLEASE READ THE RULES BEFORE STARTING THE GAME!")
mixer.music.load("Sounds\\Plz read the rules.mp3")
mixer.music.play()
time.sleep(2.9)

print("RULE 1:-\nThere are 5 rounds in this game and in each round 2 "
      "random statements will be given to you; You have to\nanswer whether"
      " they are True or False; If your answer is correct, you will be rewarded by 1 point.")
mixer.music.load("Sounds\\rule1.mp3")
mixer.music.play()
time.sleep(11.7)

print("RULE 2:-\nPlease give the answer only in True or False otherwise "
      "your answer will consider as wrong.")
mixer.music.load('Sounds\\rule2.mp3')
mixer.music.play()
time.sleep(6.8)

while True:
    print("Type \'Ready\' to start the Game:")
    mixer.music.load("Sounds\\Type ready.mp3")
    mixer.music.play()
    time.sleep(1)

    a = input()
    if a.upper() == "READY":
        quiz_game()
        time.sleep(1)
        print("\nDO YOU WANT TO PLAY THE GAME AGAIN(YES/NO)?")
        mixer.music.load("Sounds\\do you like to play the game again.mp3")
        mixer.music.play()
        time.sleep(1)
        b = input()
        if len(b) == 0:
            while len(b) == 0:
                print("Please write the answer!")
                mixer.music.load("Sounds\\please write the answer..mp3")
                mixer.music.play()
                time.sleep(1)
                b = input()
        elif b.upper() == "YES":
            pass
        else:
            break
    else:
        print("Please type Ready correctly!")
        mixer.music.load("Sounds\\plz type ready correctly.mp3")
        mixer.music.play()
        time.sleep(1.7)
