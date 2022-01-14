from random import randint 
import time 

def rps():
    leader_list = []
    full_leader_list = {}
    player_score_dict= {}
    while True:
        computer_list = ['rock', 'paper', 'scissors']
        name = input("What is your name? or 'exit': ").lower()
        if name.lower() == 'exit':
            break
        elif name.lower() not in player_score_dict:
            player_num = name.lower()
            leader_list.append(player_num)
            name_dict = {name:0, "Computer":0}
            player_score_dict[player_num]= name_dict
            print(f"Welcome {name.title()} to Rock, Paper, Scissors Python Edition")
        else:
            print(f"Welcome back {name.title()} to Rock, Paper, Scissors Python Edition")
        
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nSelect one of the following: ")
            print("[Rules]\n[Play]\n[Leaderboard]\n[Quit]")
            option = input()
            
            if option.lower() == 'rules':
                print("The rules are simple... select either rock, paper, or scissors\nand play against the world's best computer.\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock")
                continue
            elif option.lower() == 'leaderboard':
                print(f"===========\nLeaderboard:")
                for leader in leader_list:
                    if (player_score_dict[leader][leader]+player_score_dict[leader]["Computer"]) != 0:
                        player_winrate = (player_score_dict[leader][leader]/((player_score_dict[leader][leader]+player_score_dict[leader]["Computer"]))*100)
                        print(f"{leader.title()} : {int(player_winrate)} %")
                    else:
                        print(f"{leader.title()} : N/A")
                print("===========")
                continue
            elif option.lower() == 'play':
                print(f"The score is {name.title()} {player_score_dict[player_num][name]} : Computer {player_score_dict[player_num]['Computer']} ")
                while True:
                    select = input("Choose either rock, paper, scissors or cancel[c] to return to the main menu: ")
                    computer_choice = computer_list[randint(0,2)]
                    if (select.lower() == 'rock') or (select.lower() == 'paper') or (select.lower() == 'scissors'):
                        time.sleep(.7)
                        print("rock..")
                        time.sleep(.7)
                        print("paper..")
                        time.sleep(.7)
                        print("scissors..")
                        time.sleep(.7)
                        print("SHOOT!")
                        if select.lower() == computer_choice:
                            print(f"Computer plays {computer_choice}\nDraw")
                        elif (select.lower() == "rock" and computer_choice == "scissors") or (select.lower() == "scissors" and computer_choice == "paper") or (select.lower() == "paper" and computer_choice == "rock"):
                            print(f"Computer plays {computer_choice}\nYou Win!")
                            player_score_dict[player_num][name] += 1
                        else:
                            print(f"Computer plays {computer_choice}\nYou lose")
                            player_score_dict[player_num]["Computer"] += 1   
                        print(f"The score is {name.title()} {player_score_dict[player_num][name]} : Computer {player_score_dict[player_num]['Computer']} ")
                        continue
                    elif (select.lower() == 'c') or (select.lower() == 'cancel'):
                        print("Hope you enjoyed playing!")
                        break
                    else:
                        print("huh... lets try this again")
                        continue
            elif option.lower() == 'quit':
                print(f"Bye {name.title()}!")
                break
            else:
                print("huh... lets try this again")
                continue
            
