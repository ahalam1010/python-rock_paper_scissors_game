import random
print("Welcome to Rock Paper Scissor")

user_wins = 0
computer_wins = 0

options = [ "rock", "paper", "scissor"]

want_to_play = input("Do you want to play [y/n]? ").lower()

if want_to_play == "y":
    print("Lets Play!")

    while True:
        choice = input("Pick your choice [Rock, Paper, Scissor]? or quit for q ").lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in options:
            print("Invalid choice, try again")
            continue

        random_num = random.randint(0, 2)

        computer_picks = options[random_num]

        print(f"Computer picks {computer_picks}")


        if choice == computer_picks:
            print("It's a tie!")
        elif choice == 'rock' and computer_picks == 'scissor':
            user_wins += 1
            print("You win!")
        elif choice == 'paper' and computer_picks == 'rock':
            user_wins += 1
            print("You win!")
        elif choice == 'scissor' and computer_picks == 'paper':
            user_wins += 1
            print("You win!")
        else:
            computer_wins += 1
            print("You lose!")

        print(f"You: {user_wins} | Computer: {computer_wins}")

else:
    print("Goodbye!")
