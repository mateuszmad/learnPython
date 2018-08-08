import random

file = open("hangman.txt", "r")
line = random.choice(open('hangman.txt').readlines())
number = len(line)
print(line)

x = 1
goal = []
while x < number:
    goal.append("_")
    x += 1
print(" ".join(goal))

points = 0
lose_points = 0
while True:
    control = 0
    letter_number = 0
    guess = input("Please guess the letter: ")

    for letter in line:
        if guess == letter:
            goal[letter_number] = guess
            points += 1
            control = 1
        letter_number += 1

    if control == 0:
        lose_points += 1
        print("WRONG GUESS, YOU HAVE",(5-lose_points)," GUESSES LEFT")

    print(" ".join(goal))

    if points == (len(line)-1):
        print("END OF THE GAME, YOU WIN")
        break
    elif lose_points == 5:
        print("END OF THE GAME, YOU LOSE")
        break

file.close()