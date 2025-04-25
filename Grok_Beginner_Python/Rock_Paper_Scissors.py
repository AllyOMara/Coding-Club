# Alexandria O'Mara
# Welcome to rock paper scissors
# The comments will guide you through what does what.
# Enjoy and happy coding

# Importing random (used here to generate random integers) and time (for delayed actions)
import random
import time


# ASCII ART OF CHOICES
rock_pic = """
                        ,-.        _.---._        
                        |  `\.__.-''       `.    
                         \  _        _  ,.   \    
   ,+++=._________________)_||______|_|_||    |  
  (_.ooo.===================||======|=|=||    |  
     ~~'                 |  ~'      `~' o o  /    
                          \   /~`\     o o  /    
                           `~'    `-.____.-'      \n"""
scissors_pic = """
     |\    /|
     \\\\  //
      \\\\//
       )(
      //\\\\
     _//  \\\\_
     /  \  /  \.
     \__/  \__/ \n"""
paper_pic = """
    __________
    |        |
    | I AM   |
    |A SHEET |
    |OF PAPER|
    |________| \n"""


# INTRODUCTION
name = input("What is your name? ")
time.sleep(0.2)
print("\n\n-------------------------------------------------------")
time.sleep(1)
print("Welcome, " + name + ", to Human vs. Computer in Scissors, Paper, Rock!")
time.sleep(1)
print("-------------------------------------------------------")
time.sleep(1)
print("Moves: choose scissors paper or rock by typing in your selection. Entering quit will end the game.")
time.sleep(1)
print("Rules: scissors cuts paper, paper covers rock and rock crushes scissors.")
time.sleep(1)
print("Good luck!")
time.sleep(1)
print("--------------------------------------------------------")
time.sleep(2)


# Determining the number of games played (first to how many points?)
number_games = input("To start off, how many points is needed to win? (Please choose between 1 and 100.) ")
if str(number_games).lower() == "quit":
    print("GAME OVER!")
    quit()

number_games = int(number_games)
no_o_games = 1


# Scoring system
human_points = 0
computer_points = 0
while (human_points != number_games) and (computer_points != number_games):
    # Defining the computer's move
    computer_move = random.choice(["scissors", "paper", "rock"])
    print("Game number " + str(no_o_games))

    # Defining the player's move while preventing them from saying anything other than rock, paper, and scissors
    human_move = input("What is your move? Scissors, paper or rock? ")
    while (human_move.lower() != "scissors") and (human_move.lower() != "paper") and (human_move.lower() != "rock") and (human_move.lower() != "quit"):
        human_move = input("That is not a valid move. Please choose between scissors, paper and rock. Please note that your answer can not include spaces.")

    if human_move.lower() == "quit":
        print("\n\nGAME OVER!")
        print("Human won " + str(human_points) + " points.")
        print("Computer won " + str(computer_points) + " points.")
        if human_points > computer_points:
            print(name + " is the winner! \(￣︶￣*\)")
            quit()
        if computer_points > human_points:
            print("Computer is the winner! (┬┬﹏┬┬)")
            quit()
        if computer_points == human_points:
            print("Draw! No one is the winner ヾ(≧へ≦)〃")
            quit()

    # Printing the player's and computer's moves
    time.sleep(0.5)
    print("Computer played: " + computer_move)
    if computer_move == "rock":
        time.sleep(1)
        print(rock_pic)
    if computer_move == "paper":
        time.sleep(1)
        print(paper_pic)
    if computer_move == "scissors":
        time.sleep(1)
        print(scissors_pic)

    time.sleep(0.5)
    print(name + " played: " + human_move)
    if human_move == "rock":
        time.sleep(1)
        print(rock_pic)
    if human_move == "paper":
        time.sleep(1)
        print(paper_pic)
    if human_move == "scissors":
        time.sleep(1)
        print(scissors_pic)

    # Finding who is the winner
    results = { ("scissors", "scissors"): "draw", ("scissors", "paper"): "human", ("scissors", "rock"): "computer", ("paper", "scissors"): "computer", ("paper", "paper"): "draw", ("paper", "rock"): "human", ("rock", "scissors"): "human", ("rock", "paper"): "computer", ("rock", "rock"): "draw" }
    winner = results [(human_move.lower(), computer_move.lower())]

    # Printing the winner of the round
    if winner == "human":
        time.sleep(1)
        print("Human won! 1 point to the human.")
        human_points = human_points + 1
    if winner == "computer":
        time.sleep(1)
        print("Computer won! 1 point to the computer.")
        computer_points = computer_points + 1
    if winner == "draw":
        time.sleep(1)
        print("No one won! No points have been given.")
    no_o_games = no_o_games + 1

# Overall winner
print("\n\nGAME FINISHED!")
print("Human won " + str(human_points) + " points.")
print("Computer won " + str(computer_points) + " points.")
if human_points == number_games:
    print(name + " is the winner! \(￣︶￣*\)")
if computer_points == number_games:
    print("Computer is the winner! (┬┬﹏┬┬)")
    time.sleep(5)
    print("Now entering...")
    time.sleep(5.5)
    print("the matrix.\n\n")
    time.sleep(5)
    exit

# END OF PROGRAM
