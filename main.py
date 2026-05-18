from src.game_logic import NumberGame

def main(): 
    game = NumberGame()
    game.new_game()

    print("🎯 Guess the number between 0 and 100!")
    print("Type 'quit to exit.\n")

    while not game.won:
        user_input = input("Your guess: ").strip()

        if user_input.lower() == 'quit': 
            print("Thnaks for playing!")
            return
        
        status, message = game.validate(user_input)

        # Dramatic pause...
        if status in ('high', 'low'):
            print("Thinking...")
            import time
            time.sleep(0.5)

        print(message)

    print("\nGame Over. Play again soon!")

if __name__ == "__main__":
    main()
