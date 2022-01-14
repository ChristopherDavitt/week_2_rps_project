from random import randint 
import module



def rps(p1, p2):
    player_score_dict= {}
    while True:
        
        name = input("What is your name?: ")
        if name.lower() not in player_score_dict:
            player_num = name
            name_dict = {name:0, "Computer":0}
            player_score_dict[player_num]= name_dict
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
                while True:
                    select = input("Choose either rock, paper, scissors or cancel[c] to return to the main menu ")
                    if select.lower() == 'rock':
                        result(select)
                    elif select.lower() == 'paper':
                        result(select)
                    elif select.lower() == 'scissors':
                        result(select)
                    elif select.lower() == 'c':
                        continue
                    else:
                        print("huh... lets try this again")
            

    

rps("name","name")

    
