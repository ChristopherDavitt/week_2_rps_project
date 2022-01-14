def result(player):
    computer_list = ['rock', 'paper', 'scissors']
    computer_choice = computer_list[randint(0,2)]
    if player == computer_choice:
        print("Draw")
        print(f"The score is {name} {player_score_dict[player_num][name]} : Computer {player_score_dict[player_num]['Computer']} ")
    elif (player.lower() == "rock" and computer_choice == "scissors") or (player.lower() == "scissors" and computer_choice == "paper") or (player.lower() == "paper" and computer_choice == "rock"):
        print("You Win!")
        player_score_dict[player_num][name] += 1
        print(f"The score is {name} {player_score_dict[player_num][name]} : Computer {player_score_dict[player_num]['Computer']} ")
    else:
        print("You lose")
        player_score_dict[player_num]["Computer"] += 1
        print(f"The score is {name} {player_score_dict[player_num][name]} : Computer {player_score_dict[player_num]['Computer']} ")