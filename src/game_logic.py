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

    def new_game(self, forced_target=None):
        """
        Start a fresh round & testing environment
        """
        if forced_target is not None:
            self.target = forced_target
        else:
            self.target = random.randint(self.min_val, self.max_val)

        self.attempts = 0
        self.start_time = time.time()
        self.history = []
        self.won = False

    def get_temperature(self, distance):
        """
        Return (status, message) based on distance from target.
        NO side effects.
        """
        if distance == 0:
            return 'correct', "🎯 Correct!"
        elif distance <=3:
            return 'fire', "🔥 Fire!"
        elif distance <=10:
            return 'warm', "♨️ Warm!"
        elif distance <=21:
            return 'mild', "⛅ Mild!"
        elif distance <=52:
            return 'cold', "☃️ Cold!"
        else:
            return 'freezing', "🧊 FREEZING"        

    def validate(self, guess_input):
        """
        Returns a tuple: (status, message)
        status can be: 'correct', 'fire', 'warm', 'mild', 'cold', 'freezing', 'invalid'
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
        
        # 4. Valid Number
        self.attempts += 1
        self.history.append(number)

        distance = abs(self.target - number)
        status, message = self.get_temperature(distance)

        if status == 'correct':
            self.won = True
            elapsed = time.time() - self.start_time
            message = f"🎯 Correct! You won in {self.attempts} attempts and {elapsed:.1f} seconds!"

        return status, message
