import time
from getpass import getpass
print("---------------------------------------")
print("Rock Paper Scissor Game By Rishabh Jain")
print("---------------------------------------")
print("Vesrion 2.0")
print("---------------------------------------")
username_list=[]
password_list=[]
def single_player():
    lives=5
    score=0
    draws=0
    computer_lives=5
    while True:
        c=input("Rock, Paper, Scissors??  ").capitalize()
        import random
        computer=("Rock","Paper","Scissors")
        computer=random.choice(computer)
        # Rock statements
        if c=="Rock" and computer=="Paper":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("Computer Wins!!")
            print("")
            print("")
            lives-=1
        if c=="Rock" and computer=="Scissors":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("You Win!!")
            computer_lives-=1
            print("")
            print("")
            score+=1
        # Paper statements
        if c=="Paper" and computer=="Scissors":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("Computer Wins!!")
            print("")
            print("")
            lives-=1
        if c=="Paper" and computer=="Rock":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("You Win!!")
            computer_lives-=1
            print("")
            print("")
            score+=1
        # Scissor statements
        if c=="Scissors" and computer=="Rock":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("Computer Wins!!")
            print("")
            print("")
            lives-=1
        if c=="Scissors" and computer=="Paper":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("You Win!!")
            computer_lives-=1
            print("")
            print("")
            score+=1
        # Draw statements
        if c=="Rock" and computer=="Rock":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("It's a Draw")
            print("")
            print("")
            draws+=1
        if c=="Paper" and computer=="Paper":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("It's a Draw")
            print("")
            print("")
            draws+=1
        if c=="Scissors" and computer=="Scissors":
            print("")
            print("The Computer chooses", computer)
            print("")
            print("It's a Draw")
            print("")
            print("")
            draws+=1
        # Wrong input
        if c not in ("Rock","Paper","Scissors","Lives","Score","Draws","Exit"):
            print("")
            print("Wrong input, Please try again")
            print("")
        # System statements
        if c=="Rules":
            print("**********************************************")
            print("Rules")
            print("**********************************************")
            print("-Rock looses against Paper")
            print("-Rock beats Scissors")
            print("-Paper looses against Scissors")
            print("-Paper beats Rock")
            print("-Scissors looses against Rock")
            print("-Scissors beats Paper")
            print("**********************************************")
        if c=="Lives":
            print(lives)
        if c=="Score":
            print(score)
        if c=="Draws":
            print(draws)
        
        # Lives
        if lives==0:
            print("Thanks for playing")
            print("You have ran out of lives")
            print("Your score=", score)
            print("You drew", draws ,"times")
            stop=input("Press Enter to exit.")
            exit()
        if computer_lives==0:
            print("Thanks for playing")
            print("The computer has ran out of lives. You Win!!")
            print("Your score=", score)
            print("You drew", draws ,"times")
            stop=input("Press Enter to exit.")
            exit()

        # Exit
        if c.lower()=="exit":
            exit()
            
def multi_player():
    player1_lives=5
    player2_lives=5
    player1_score=0
    player2_score=0
    draws=0
    while True:
        c1=getpass("Player 1: Rock ,Paper, Scissors??  ").capitalize()
        c2=getpass("Player 2: Rock, Paper, Scissors??  ").capitalize()
        # Rock statements
        if c1=="Rock" and c2=="Paper":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("Player 2 Wins!!")
            print("")
            print("")
            player1_lives-=1
            player2_score+=1
        if c1=="Rock" and c2=="Scissors":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("Player 1 Wins!!")
            print("")
            print("")
            player2_lives-=1
            player1_score+=1
        # Paper statements
        if c1=="Paper" and c2=="Scissors":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("Player 2 Wins!!")
            print("")
            print("")
            player1_lives-=1
            player2_score+=1
        if c1=="Paper" and c2=="Rock":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("Player 1 Wins!!")
            print("")
            print("")
            player2_lives-=1
            player1_score+=1
        # Scissor statements
        if c1=="Scissors" and c2=="Rock":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("Player 2 Wins!!")
            print("")
            print("")
            player1_lives-=1
            player2_score+=1
        if c1=="Scissors" and c2=="Paper":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("Player 1 Wins!!")
            print("")
            print("")
            player2_lives-=1
            player1_score+=1
        # Draw statements
        if c1=="Rock" and c2=="Rock":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("It's a Draw")
            print("")
            print("")
            draws+=1
        if c1=="Paper" and c2=="Paper":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("It's a Draw")
            print("")
            print("")
            draws+=1
        if c1=="Scissors" and c2=="Scissors":
            print("")
            print("Player 1 chooses", c1)
            print("")
            print("Player 2 chooses", c2)
            print("")
            print("It's a Draw")
            print("")
            print("")
            draws+=1
        # Wrong input
        if (c1 or c2) not in ("Rock","Paper","Scissors","Lives","Score","Draws","Exit"):
            print("")
            print("Wrong input, Please try again")
            print("")
        # System statements
        if c1=="Rules" or c2=="Rules":
            print("**********************************************")
            print("Rules")
            print("**********************************************")
            print("-Rock looses against Paper")
            print("-Rock beats Scissors")
            print("-Paper looses against Scissors")
            print("-Paper beats Rock")
            print("-Scissors looses against Rock")
            print("-Scissors beats Paper")
            print("**********************************************")
        if c1=="Lives":
            print(player1_lives)
        if c1=="Score":
            print(player1_score)
        if c2=="Lives":
            print(player2_lives)
        if c2=="Score":
            print(player2_score)
        if c1=="Draws" or c2=="Draws":
            print(draws)
        
        # Lives
        if player1_lives==0:
            print("Thanks for playing")
            print("Player 1 ran out of lives. Player 2 Wins!!")
            print("Player 1 score=", player1_score)
            print("Player 2 score=", player2_score)
            print("You drew", draws ,"times")
            stop=input("Press Enter to exit.")
            exit()
        if player2_lives==0:
            print("Thanks for playing")
            print("Player 2 has ran out of lives. Player 1 Wins!!")
            print("Player 1 score=", player1_score)
            print("Player 2 score=", player2_score)
            print("You drew", draws ,"times")
            stop=input("Press Enter to exit.")
            exit()

        # Exit
        if c1=="Exit" or c2=="Exit":
            exit()

while True:
    print("To begin, fill the below information")
    username=getpass("Please enter your username  ")
    password=getpass("Please enter your password  ")
    search_file_P=open("Rock Paper Scissor Game Passwords.txt","r")
    search_file_U=open("Rock Paper Scissor Game Username.txt","r")
    for line in search_file_P:
        password_list.append(line.strip())
    for line in search_file_U:
        username_list.append(line.strip())
    if (password in password_list) and (username in username_list):
        time.sleep(0.5)
        print("Loading....")
        time.sleep(0.5)
        print("Loading....")
        time.sleep(0.5)
        print("Loading....")
        time.sleep(0.5)
        print("Access Granted!!")
        
    else:
        print("Your username or password is incorrect. Please try again")
        print("--------------------------------------------------------")
        exit()

    start_menu="""
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     ___                  ______________     ______________     _______________     ____      ___                                            
    ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /                                           
 /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /                                            
/                  ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /                                             
¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /                                              
¦       \-----------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /                                               
¦                  ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \                                               
¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \                                              
¦       \-----------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___        
¦                  ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦       
¦       ------------                                                                                              ¦   ¦¦   ¦¦   ¦¦   ¦       
\       \-----------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦       
 \                 /                                                                                         ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
  \---------------/  ___________     _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /       
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /        
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /         
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /                              _____
                    ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                             /     /
 ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________                   /     /
¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ___________ /     /
¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /          /     /
¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦         /     /
¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /
             ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               ________________
             ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                               ¦
 ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               ________________¦
¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦       
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
    start_menu_="""
---------------------------------------------
Rules:
You start with 5 lives.
If you win, you get a point.
If you loose, you loose a life.
If you draw, the lives stay the same.
---------------------------------------------
To see a list of rules type "rules".
---------------------------------------------
At any point type "exit" to leave the game.
---------------------------------------------
To see your current lives, type "lives".
---------------------------------------------
To see your current score, type "score".
---------------------------------------------
To see number of draws, type "draws".
---------------------------------------------
"""
    print(start_menu)
    time.sleep(0.5)
    print(start_menu_)
    time.sleep(0.5)
    print("Which mode you want to play??:")
    print("")
    print("1: V/S Computer \n2: V/S Friend \n")
    ch=int(input("Enter your choice  "))
    print("")
    if ch==1:
        single_player()
    elif ch==2:
        multi_player()
