import random

class guessTheNumber: 

    randomNumber = 0

    """
    Wählen eine random Zahl aus.
    """
    def pickNumber(self):

        self.randomNumber = random.randint(0,100)
        print(self.randomNumber)
        

    """
    
    """

    def letsPlay(self, randomNumber):
        print("Hello Player. Wanna play a Game?")
        print("I am gonna choose a Number and you are gonna try and guess the Number I have choosen.")
        print("Let's play. Make your first guess: ")