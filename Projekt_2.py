"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michal Krejčí
email: don.night@post.cz
discord: donnight
"""


import random
import time

def generate_secret_number():
    secret_number = []
    secret_number.append(random.randint(1,9))

    while True:
        random_number = random.randint(0,9)
        if random_number in secret_number:
            continue
        secret_number.append(random_number)
        if len(secret_number) == 4:
            break

    # print(secret_number)
    return(secret_number)

def user_test():
    while True:
        test = input(">>> ")
        if len(test) != 4 or not test.isdigit() or len(set(test)) != 4 or test[0] == "0":
            print("Enter a 4 digit number with unique digits and not beginning with zero.")
        else:
            break

    return test

def counting_numbers(secret_number, test):
    bulls = 0
    cows = 0
    test_list = [int(i) for i in str(test)]
    for i in range(4):
        if test_list[i] == secret_number[i]:
            bulls += 1
        elif test_list[i] in secret_number:
            cows += 1

    return bulls, cows

def game():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a Bulls and Cows game.")
    print("-" * 47)
    print("Enter a number:")
    print("-" * 47)

    secret_number = generate_secret_number()
    try_count = 0
    time_start = time.time()

    while True:
        test = user_test()
        bulls, cows = counting_numbers(secret_number, test)
        try_count += 1

        if bulls == 4:
            time_end = time.time()
            time_count = round(time_end - time_start, 0)
            count_text = "guess" if try_count == 1 else "guesses"
            print("-" * 47)
            print(f"Correct, you've guessed the right number in {try_count} {count_text}!")
            print(f"It took {time_count} seconds.")

            if try_count == 1:
                print("That's amazing!")
            elif try_count <= 10:
                print("That's very good!")
            elif try_count <= 20:
                print("That's good!")
            else:
                print("Not so good.")
            break

        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_text}, {cows} {cow_text}")

    return time_count, try_count

def main():
    time_stat = []
    try_stat = []
    game_count = 1

    while True:
        time_count, try_count = game()
        time_stat.append(time_count)
        try_stat.append(try_count)
        print("-" * 47)
        next_game = input("For next game enter Y: ")
        if next_game.upper() == "Y":
            game_count += 1
            continue
        else:
            break

    game_count_text = "game" if game_count == 1 else "games"
    print("-" * 47)
    print(f"You played {len(try_stat)} {game_count_text}.")
    print(f"One average game lasted for {round(sum(time_stat)/len(time_stat), 2)} seconds.")
    print(f"One average game requires {round(sum(try_stat)/len(try_stat), 2)} guesses.")

if __name__ == "__main__":
    main()
