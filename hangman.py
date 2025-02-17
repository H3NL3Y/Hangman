#Hangman
import random

def win():
    print("YOU GUESSED THE WORD!")
def hanged():
    print("YOU HAVE BEEN HANGED!")

def play(word):
    guessedLetters = []

    fullWord = "_"*len(word) #Creates placeholder for word using _
    print(fullWord)

    count = 6
    while True:
        display = ""
        guess = input("Enter your guess: ").lower()
        if guess == word: #Allows user to guess full word.
            win()
            break
        for letter in word: #Checks each letter in word.
            if letter in guessedLetters:
                display += letter #If matched it will add letter to display
            elif letter == guess:
                guessedLetters.append(guess)
                display += guess
            else:
                display += "_" #If no match then add _
        if guess not in display:
            print("Letter not in word.")
            guessedLetters.append(guess)
            count -= 1
            print(f"You have {count} lives left!")
            print(guessedLetters)


        print(display)
        if count == 0: #Provides 7 chances.
            hanged()
            break
        elif display == word:
            win()
            break

# TODO:: Find location of the found letter. COMPLETE
# TODO:: Replace letters to _ and replace when found. COMPLETE
# TODO:: Check win/loss condition. COMPLETE
# TODO:: Allow user to guess full word. COMPLETE
# TODO:: Only lose lives if wrong letter is chosen. <---

#Choose random word.

with open("wordList.txt", "r") as file:
	allText = file.read()
	words = list(map(str, allText.split()))

	# print random string
	word = random.choice(words)

word.lower()
print(word)
play(word)
