import random
import time

class NumberGame:
    def __init__(self, min_val=0, max_val=100):
        self.min_val = min_val
        self.max_val = max_val
        self.target = None
        self.attempts = 0
        self.start_time = 0
        self.history = []
        self.won = False

    def new_game(self):
        """Start a fresh round."""
        self.target = random.randint(self.min_val, self.max_val)
        self.attempts = 0
        self.start_time = time.time()
        self.history = []
        self.won = False

    def validate(self, guess_input):
        """
        Returns a tuple: (status, message)
        status can be: 'correct', 'high', 'low', 'invalid'
        """
        # 1. Try to convert to integer
        try:
            number = int(guess_input)
        except ValueError:
            # Check for float
            try:
                float(guess_input)
                return 'invalid', "No decimals allowed! Whole numbers only."
            except ValueError:
                return 'invalid', "That's not a number!"
        
        # 2. Check negatives
        if number < 0:
            return 'invalid', "No negatives allowed!"
        
        # 3. Check range
        if number < self.min_val or number > self.max_val:
            return 'invalid', f"Must be between {self.min_val} and {self.max_val}"
        
        # 4. Valid number processor
        self.attempts += 1
        self.history.append(number)

        if number == self.target:
            self.won = True
            elapsed = time.time() - self.start_time
            return 'correct', f"Correct! You won in {self.attempts} attempts and {elapsed:.1f} seconds!"
        elif number > self.target:
            return 'high', "Too high! Try a bit lower..."
        else: 
            return 'low', "Too low! Try a bit higher..."