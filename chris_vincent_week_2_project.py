from random import randint 

def rps(p1, p2):
    computer_list = ['rock', 'paper', 'scissors']
    player_score_dict= {

    }
    name = input("What is your name?: ")
    print(f"Welcome {name} to Rock, Paper, Scissors Python Edition")
    while True:
        option = input("Select one of the following\
            [Rules]\
            [Play]\
            [Quit]")
        if option.lower() == 'rules':
            print("The rules are simple... select either rock, paper, or scissors\
                    and play against the world's best computer.\
                    Rock beats Scissors\
                    Scissors beats Paper\
                    Paper beats Rock")
            continue
        elif option.lower() == 'play':
            select = input("Choose either rock, paper, scissors or cancel[c] to return to the main menu ")
            if select.lower() == 'rock':
                computer_choice = computer_list[randint(0,2)]
                if computer_choice == 'rock':
                    print("Draw")
                elif computer_choice == 'paper':
                    print("You lose")
                elif computer_choice == 'scissors':
                    print("You Win!")
            player_score_dict[name] =        
            elif select.lower() == 'paper':
                computer_choice = computer_list[randint(0,2)]
            elif select.lower() == 'scissors':
                computer_choice = computer_list[randint(0,2)]
            elif select.lower() == 'c':
                continue
            else:
                print("huh... lets try this again")
        

    

rps("name","name")

    