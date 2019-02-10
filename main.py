# Import
import random
# Define class 
class Lottery(object):   
    def __init__(self, numbers=list(range(49)), answer=None):
        self.numbers = numbers
        self.answer = answer
        if answer is None:
            self.answer= random.choice(self.numbers)
        # self.answer = answer

    def get_answer(self):
        return self.answer
    
    def play(self, number_given):
        if number_given in self.numbers:
            return True
        return False
