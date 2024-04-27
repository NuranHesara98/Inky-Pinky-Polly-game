import random 
player_score = 0
computer_score = 0
while True:
   
    choices = ["Inky", "Pinky", "Polly"]
    computer_choice = random.choice(choices)
    player_choice = input("Enter your choice (Inky, Pinky, or Polly): ")
    if player_choice == computer_choice:
        print("The game is tied. Both players chose", player_choice + ".")
    else:
        if player_choice == "Pinky":

            if computer_choice == "Inky":
                print("Player wins! Computer choice was", computer_choice + ".")
                player_score += 1
            else:
                print("Computer wins! Computer choice was", computer_choice + ".")
                computer_score += 1
        elif player_choice == "Inky":
            if computer_choice == "Polly":
                print("Player wins! Computer choice was", computer_choice + ".")
                player_score += 1
            else:
                print("Computer wins! Computer choice was", computer_choice + ".")
                computer_score += 1
        else:
            if computer_choice == "Pinky":
                print("Player wins! Computer choice was", computer_choice + ".")
                player_score += 1
            else:
                print("Computer wins! Computer choice was", computer_choice + ".")
 
    user_input = input("Do you want to play again? (y/n): ")
    if user_input.lower() == "y":
        print("Let's play again!")
    elif user_input.lower() == "n":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

print("Player score:", player_score)
print("Computer score:", computer_score)

if player_score > computer_score:
    print("Player wins the game!")
elif player_score < computer_score:
    print("Computer wins the game!")
else:
    print("The game is tied!")
