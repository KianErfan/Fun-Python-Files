from random import randint

t = ("Rock", "Paper", "Scissors")


def play_game():
    computer = t[randint(0, 2)]
    player = False
    while not player:
        player = input("Pick one rock, paper or scissors?: ").lower()
        if player == computer:
            print("Tie, Try Again Next Time")
        elif player == "rock":
            if computer == "paper":
                print("You Lose", computer, "Beats", player)
            else:
                print("Enemy Conquered", player, "Beats", computer)
        elif player == "paper":
            if computer == "scissors":
                print("You Lose", computer, "Beats", player)
            else:
                print("Good Job", player, "Beats", computer)
        elif player == "scissors":
            if computer == "rock":
                print("You Lose", computer, "Beats", player)
            else:
                print("You Win", player, "Beats", computer)
        else:
            print("Error, Shutting Down.")


isPlaying = True
while isPlaying:
    answer = input("Do you want to play? Yes/No: ").lower()
    if answer == "yes":
        play_game()
    else:
        isPlaying = False
        print("Bye!")
