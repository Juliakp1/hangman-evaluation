import random, requests
from re import match # allows regex in list

# -------------- #
# Word pool
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
r = requests.get(url, allow_redirects=True)
content = str(r.content.decode()).split('\n')
# -------------- #

# We need to remove words like 'Adhemar', because its not lowercase
b=0
for i in range(len(content)):
    if (content[i-b] != content[i-b].lower()):
        content.remove(content[i-b])
        b+=1

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

class Hangman:
    def __init__(self):
        
        if r.status_code==200:
            self.content = content
        else:
            print("Erro: ", r.status_code)
    
    # ----------------------------- #

    def new_game(self, lifes=5):
        self.running = True
        self.lifes = lifes
        self.word = random.choice(self.content)
        return len(self.word)
    
    # ----------------------------- #

    def guess_letter(self, letter):
        if self.lifes > 0:
            if letter in self.word:
                return [idx for idx in range(len(self.word)) if self.word[idx]==letter]
            else:
                self.lifes -= 1
                if self.lifes == 0:
                    self.running = False
                    return False
                else:
                    return []
    
    # ----------------------------- #

    def guess_word(self, word):
        if self.lifes > 0:
            if self.word == word:
                self.running = False
                return True
            else:
                self.lifes = 0
                self.running = False
                return False
            
    # ----------------------------- #

    def check_word(self, word):
        if self.word == word:
            return True
        return False

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def absolute_probability(chosenWord):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    probabilities = {letter:0 for letter in alphabet}

    # adds 1 for every time that letter appears
    for word in content:
        for letter in word:
            probabilities[letter.lower()] += 1

    # Orders the probabilities
    probabilities = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))
    keysProbs = list(probabilities.keys())

    # starts game
    game = Hangman()
    game.new_game()  
    game.word = chosenWord
    letters = len(game.word)

    # makes a list to save the guesses
    guessList = []
    for i in range(letters):
        guessList.append('.')

    curLetter = 0 
    while game.running:

        # guesses a letter and saves it 
        print(guessWord, '- guess: ', keysProbs[curLetter]) 
        letterSpots = game.guess_letter(keysProbs[curLetter])
        if type(letterSpots) != bool:
            for numbs in letterSpots:
                guessList[numbs] = keysProbs[curLetter]
            curLetter+=1

        # checks if the word is already guessed
        guessWord = ''.join(guessList)
        gotWord = game.check_word(guessWord)
        if gotWord:
            break
    print(guessWord)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def get_new_guess(guessList, currentAlphabet):

    probabilities = {letter:0 for letter in currentAlphabet}

    # gets all the words that fit this situation
    filterRegex = ''.join(guessList)
    possibleWords = list(filter(lambda v: match(filterRegex, v), content))

    # gets words that fit into the current alphabet, and lenght
    filterRegex = '^['+currentAlphabet+']{'+str(len(guessList))+'}$'
    avaliableWords = list(filter(lambda v: match(filterRegex, v), possibleWords))

    # adds 1 for every time that letter appears
    for word in avaliableWords:
        for letter in word:
            if (letter in currentAlphabet) and (letter not in guessList):
                probabilities[letter.lower()] += 1

    # gets the key of the hight value in dict
    nextGuess = max(probabilities, key=probabilities.get)
    return nextGuess

# ---------------------------------------------- #

def letter_by_round(word):

    game = Hangman()
    game.new_game()  
    game.word = word
    letters = len(game.word)

    # makes a list to save the guesses
    guessList = []
    for i in range(letters):
        guessList.append('.')
    guessWord = ''.join(guessList)

    nextGuess = 'a'
    currentAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    while game.running:

        # guesses a letter and saves it 
        print(guessWord, '- guess: ', nextGuess) 
        letterSpots = game.guess_letter(nextGuess)
        
        # saves the guessed (and spots) letter to the list
        if type(letterSpots) != bool:
            for numbs in letterSpots:
                guessList[numbs] = nextGuess

            # removes guessed letter from alphabet if its wrong
            if letterSpots == []:
                currentAlphabet = currentAlphabet.replace(nextGuess,'')

            # checks if the word is already guessed
            guessWord = ''.join(guessList)
            gotWord = game.check_word(guessWord)
            if gotWord:
                break

            # gets the next guess
            nextGuess = get_new_guess(guessList, currentAlphabet)
    print(guessWord)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

print('This file lets you test the different algs')
print('Choose one: ')
print('1 - absolute_probability')
print('2 - letter_by_round')

chosen = int(input(''))
word = input('Chose word: ')

if (chosen == 1):
    absolute_probability(word)
if (chosen == 2):
    letter_by_round(word)
