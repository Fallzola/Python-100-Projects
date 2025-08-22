import random
wordList = ['apple', 'banana', 'beach', 'bicycle', 'brain', 'bubble', 'camera', 'candy', 'castle', 'chair', 'cheese', 'circle', 'cloud', 'coffee', 'cookie', 'dance', 'diamond', 'dolphin', 'dragon', 'dream', 'earth', 'egg', 'elephant', 'family', 'flower', 'forest', 'friend', 'garden', 'ghost', 'giggle', 'giraffe', 'glasses', 'grape', 'green', 'guitar', 'happy', 'heart', 'holiday', 'honey', 'horse', 'house', 'island', 'jelly', 'juice', 'jungle', 'kitten', 'koala', 'laugh', 'lemon', 'light', 'magic', 'monkey', 'mountain', 'music', 'ninja', 'ocean', 'orange', 'pancake', 'party', 'penguin', 'phone', 'piano', 'pirate', 'pizza', 'planet', 'potato', 'puppy', 'purple', 'puzzle', 'queen', 'quiet', 'rainbow', 'river', 'robot', 'rocket', 'salad', 'school', 'shark', 'smile', 'snake', 'space', 'sparkle', 'spider', 'star', 'storm', 'strawberry', 'summer', 'sunny', 'sushi', 'swing', 'table', 'tiger', 'train', 'treasure', 'turtle', 'unicorn', 'water', 'whale', 'window', 'wizard', 'yellow', 'zebra', 'zombie']

selectedWord = random.choice(wordList)
wordAsList = list(selectedWord)
wordLenght = len(selectedWord)
lives = 5
gameState = True
currentLetters = []
userWon = False

print(selectedWord)
print("Welcome to the HangMan!")
i = 0
while i < wordLenght:
    currentLetters.append('_')
    i += 1
print(currentLetters)


def guessLetter():
    global letterGuess
    letterGuess = input("What letter do you want to guess?")
    if len(letterGuess) > 1:
        if letterGuess.lower() == selectedWord:
            global userWon
            userWon = True
            keepPlaying()
        else:
            global lives
            lives = 0
            keepPlaying()
    letterGuess = letterGuess.lower()


def checkLetter():
    if letterGuess in wordAsList:
    
        print(f"You guessed '{letterGuess}' correctly!! 🍕")
        y = 0
        while y < len(wordAsList):
            if letterGuess in wordAsList[y]:
                currentLetters[y] = letterGuess
            y += 1
        print(currentLetters)
    else:
        print("You guessed wrong fool!")
        print(currentLetters)
        global lives
        lives -= 1


def keepPlaying():
    while gameState:
        if userWon == True:
            print("You won! Congratulations! 🍕")
            break
        elif lives <= 0:
            print("Game Over")
            break
        elif wordAsList == currentLetters:
            print("You won! Congratulations! 🍕")
            break
        else:
            guessLetter() 
            checkLetter()

keepPlaying()
