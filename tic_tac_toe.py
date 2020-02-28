
import random
import time

#game_input=["Null",'X','O','X','O','X','O','X','O','X']

def board(game_input):
	print(game_input[7]+'|'+game_input[8]+'|'+game_input[9])
	print(game_input[4]+'|'+game_input[5]+'|'+game_input[6])
	print(game_input[1]+'|'+game_input[2]+'|'+game_input[3])
	print('-----')

def player_input():
	marker=''
	while marker!='X' and marker!='O':
		marker=input('Player: Please chose your marker: ')
	if marker=='X':
		return ('X','O')
	else:
		return ('O','X')


def put_marker(game_input,marker,position):
	game_input[position]=marker

def win(game_input,marker):	
	return ((game_input[1]==game_input[2]==game_input[3]==marker) or
		   (game_input[4]==game_input[5]==game_input[6]==marker) or
		   (game_input[7]==game_input[8]==game_input[9]==marker) or
		   (game_input[3]==game_input[5]==game_input[7]==marker) or
		   (game_input[1]==game_input[5]==game_input[9]==marker) or
		   (game_input[1]==game_input[4]==game_input[7]==marker) or
		   (game_input[3]==game_input[6]==game_input[9]==marker) or
		   (game_input[2]==game_input[5]==game_input[8]==marker))

def chose_player():
	player=random.randint(1,2)
	if player ==1:
		return 'player1'
	else:
		return 'player2'

def space(game_input,position):
	return game_input[position]==' '

def full_board_check(game_input):
	for i in range(1,10):
		if space(game_input,i):
			return False
	return True

def player_choice(game_input):	
	position=0
	while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input,position):
		position=int(input('Please chose your position(1-9): '))
	return position

def play_again():
	choice=input('Would you like to play again[Y/N]: ')
	return choice=='Y'

def getBoardCopy(board):
    dupBoard = []
    for i in board:
        dupBoard.append(i)
    return dupBoard
    
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if space(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def computer_choice(board, computerMarker):
    if computerMarker == 'X':
        playerMarker = 'O'
    else:
        playerMarker = 'X'
    
    # First, check if we can win in the next move
    for i in range(1, 10):
        if space(board, i):
            copy = getBoardCopy(board)
            put_marker(copy,computerMarker, i)
            if win(copy, computerMarker):
                return i
                
    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        if space(board, i):
            copy = getBoardCopy(board)
            put_marker(copy, playerMarker, i)
            if win(copy, playerMarker):
                return i
    
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if space(board, 5):
        return 5
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def play_game(l):

    p1=l[0]
    p2=l[1]
    the_board=[' ']*10
    player1,player2=player_input()
    print(f"{player1} is {p1} sign")
    print(f"{player2} is {p2} sign")
    turn=chose_player()
    if turn=='player1':
        x=p1
    else:
        x=p2
    print(f'{x} will play first')
    play_game=input('Ready to play[Y/N]: ')
    if play_game=='Y':
        game_on=True
    else:
        game_on=False
        
    while game_on:
        if turn=='player1':
            board(the_board)
            position=player_choice(the_board)
            put_marker(the_board,player1,position)
            if win(the_board,player1):
                board(the_board)
                print(f'{p1} has won')
                game_on=False
            else:
                if(full_board_check(the_board)):
                    board(the_board);
                    print('Game Tie')
                    game_on=False
                else:
                    turn='player2'
        else:
            board(the_board)
            if(p2=='Computer'):
                print('Computer Turn!')
                time.sleep(1)
                position=computer_choice(the_board,player2)
            else:
                position=player_choice(the_board)
            put_marker(the_board,player2,position)
            if win(the_board,player2):
                board(the_board)
                print(f'{p2} has won')
                game_on=False
            else:
                if(full_board_check(the_board)):
                    board(the_board);
                    print('Game Tie')
                    game_on=False
                else:
                    turn='player1'

       

def main():
    
    while True:
        print("1 : Player vs Player\n2 : Player vs Computer\n")
        choice=0
        while(choice not in[1,2]):
            choice=int(input("Enter your choice: "))
        l=[]
        if choice == 1:
            l.append("Player1")
            l.append("Player2")
            play_game(l)
        elif choice==2:
            l.append("Player")
            l.append("Computer")
            play_game(l)
        if not play_again():
            break


if __name__ == "__main__":
    main()
    