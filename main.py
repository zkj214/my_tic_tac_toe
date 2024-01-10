def game_canvas(quadrants):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}   ".format(quadrants[0],quadrants[1],quadrants[2]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}   ".format(quadrants[3],quadrants[4],quadrants[5]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}   ".format(quadrants[6],quadrants[7],quadrants[8]))
    print("\t     |     |     ")
    print("\n")
def single_game(current_player):
    values=[" " for x in range(9)]
    player_position={'X':[],'O':[]}

    game_is_on=True
    while game_is_on:
        game_canvas(values)
        try:
            move=int(input(f"Player {current_player} turn. Which box? "))
        except ValueError:
            print("Wrong input. Try again.")
            continue
        else:
            if move < 1 or move > 9:
                print("Wrong input. Try again.")
                continue
            elif values[move-1] !=" ":
                print("Box is already filled. Try again.")
                continue
            else:
                values[move-1]=current_player
                player_position[current_player].append(move)

                if check_winner(player_position,current_player):
                    game_canvas(values)
                    print(f"Player {current_player} has won!")
                    game_is_on = False
                    return current_player

                if check_draw(player_position):
                    game_canvas(values)
                    print("It's a draw...")
                    game_is_on = False
                    return 'D'

                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'

def check_winner(player_pos,cur_player):
    winning_combination=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    for x in winning_combination:
        if all(y in player_pos[cur_player] for y in x):
            return True
    return False
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O'])==9:
        return True
    return False

def display_scoreboard(score):
    print("--------------------------------")
    print("            SCOREBOARD       ")
    print("--------------------------------")

    players = list(score.keys())
    print("   ", players[0], "    ", score[players[0]])
    print("   ", players[1], "    ", score[players[1]])

    print("--------------------------------\n")


if __name__ == "__main__":
    print("Player 1")
    player1= input("Input 1st player name: ")

    print("Player 2")
    player2 = input("Input 2nd player name: ")

    cur_player=player1

    player_choice={'X':"",'O':""}

    options=['X','O']

    score_board={player1:0, player2:0}
    display_scoreboard(score_board)

    while True:
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        try:
            choice=int(input("Choose an option: "))
        except ValueError:
            print("Wrong input. Try again.")
            print("\n")
            continue
        else:
            if choice==1:
                player_choice['X']=cur_player
                if cur_player==player1:
                    player_choice['O']=player2
                else:
                    player_choice['O'] = player1
            elif choice==2:
                player_choice['O']=cur_player
                if cur_player==player1:
                    player_choice['X']=player2
                else:
                    player_choice['X']=player1
            elif choice==3:
                print("Final Score")
                display_scoreboard(score_board)
                break
            else:
                print("Wrong choice. Try again.\n")
                continue

            winner=single_game(options[choice-1])

            if winner != 'D':
                player_name = player_choice[winner]
                score_board[player_name] = score_board[player_name] + 1

            display_scoreboard(score_board)

            # Switch player who chooses X or O
            if cur_player == player1:
                cur_player = player2
            else:
                cur_player = player1
