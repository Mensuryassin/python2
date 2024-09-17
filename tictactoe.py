def print_board(board):
    for row in board:
        print("|".join(row))
        print("_"* 5)

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
        
        if all([board[i][i] == player for i in range(3)]) or \
            all([board[i][2-i] == player for i in range(3)]):
            return True
        
        return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    players = ["X", "0"]
    current_player = 0

    print ("welcome to tic tac toe!")

    while True:
        print_board(board)
        player = players[current_player]
        print(f"player {player}'s turn.")

        try:
            row = int(input("Enter row (0,1,2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if board [row][col] != " ":
                print("that spot is already taken! try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 0 and 2.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"player {player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("Its a draw!")
            break

        current_player = 1 - current_player

tic_tac_toe()
