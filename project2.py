import random

def roll_dice():
   
    return random.randint(1, 6) + random.randint(1, 6)

def play_game():
    initial_roll = roll_dice()
    print(f"First roll: {initial_roll}")

    if initial_roll in [7, 11]:
        print("Congratulation! You win!")
        return
    elif initial_roll in [2, 3, 12]:
        print("Craps! The casino wins!")
        return
    else:
        goal = initial_roll
        print(f"Goal number is: {goal}")
        while True:
            current_roll = roll_dice()
            print(f"Rolling the dice... You rolled: {current_roll}")

            if current_roll == goal:
                print(f"Congratulation! You rolled the goal number {goal} again and win!")
                return
            elif current_roll == 7:
                print("You rolled a 7. The casino wins!")
                return

# Start the game
if __name__ == "__main__":
    play_game()
