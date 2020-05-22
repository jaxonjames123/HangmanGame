import time
from WordList import generate_word

displayWord = []
correctLetters = 0
wordToGuess = None
maxGuesses = 0
difficultyLevel = 3
lettersLeft = 0
guessedLetters = 0


def setDifficulty():
    # Set difficulty level for the game
    global difficultyLevel
    global maxGuesses
    global wordToGuess
    global lettersLeft
    invalid_input = True
    # while invalid_input:
    difficultyLevel = input(
        'Define your difficulty level (1, 2, or 3):\n Level 1: maximum of 8 letters, 16 guesses\n Level 2: maximum '
        'of 12 letters, 14 guesses\n Level 3: maximum of 20 letters, 14 guesses\n')
    difficultyLevel = int(difficultyLevel)
    if difficultyLevel == 1:
        maxGuesses = 16
        min_letters = 1
        maxLetters = 8
        wordToGuess = generate_word(min_letters, maxLetters)
        lettersLeft = len(wordToGuess) - 1
    elif difficultyLevel == 2:
        maxGuesses = 24
        min_letters = 9
        maxLetters = 12
        wordToGuess = generate_word(min_letters, maxLetters)
        lettersLeft = len(wordToGuess) - 1
    elif difficultyLevel == 3:
        maxGuesses = 28
        maxLetters = 20
        min_letters = 13
        wordToGuess = generate_word(min_letters, maxLetters)
        lettersLeft = len(wordToGuess) - 1
    else:
        print('You have input an unrecognized difficulty.\n Defaulting to level 3')
        difficultyLevel = 3
        maxGuesses = 28
        min_letters = 13
        maxLetters = 20
        wordToGuess = generate_word(min_letters, maxLetters)
        lettersLeft = len(wordToGuess)


def getDifficulty():
    return difficultyLevel


def getUserGuess():
    guess = input('Enter a letter to guess: ')
    guessedLetters.append(guess)
    return guess


def setDisplayWord(word):
    global displayWord
    for x in range(len(word)):
        displayWord.append('*')
    return displayWord


def displayNewWord(word, letter):
    global displayWord
    global correctLetters
    global lettersLeft
    for x in range(len(word)):
        if word[x] == letter:
            displayWord.pop(x)
            displayWord.insert(x, letter)
            lettersLeft = lettersLeft - 1
    return displayWord


def playHangman():
    numberOfGuesses = -1
    global guessedLetters
    global wordToGuess
    global maxGuesses
    guessedLetters = []
    setDifficulty()
    wordToGuess = wordToGuess[:-1]
    wordSolved = False
    print('Starting game of hangman at difficulty level {0}...'.format(getDifficulty()))
    # time.sleep(2)
    while not wordSolved:

        guessesLeft = maxGuesses - numberOfGuesses
        if guessesLeft > 0:
            if numberOfGuesses == -1:
                display = setDisplayWord(wordToGuess)
                print('The word to guess is: {0}'.format(''.join(display)))
                print('You have {0} guess(es) remaining'.format(guessesLeft - 1))
                numberOfGuesses += 1
            else:
                print('You have {0} guess(es) remaining'.format(guessesLeft))
                display = displayNewWord(wordToGuess, getUserGuess())
                numberOfGuesses += 1
                if lettersLeft == 0:
                    wordSolved = True
                    print(
                        "Congratulations! You've correctly guessed the word " + wordToGuess +
                        ", and you have beaten level {0} difficulty!".format(getDifficulty()))
                print('The word to guess is: {0}'.format(''.join(display)))

            print('Letters guessed: {0}\n'.format(', '.join(guessedLetters)))
        else:
            print('You ran out of guesses! the word was {0}'.format(wordToGuess))
            wordSolved = True


playHangman()
