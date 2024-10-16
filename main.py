def printBoard(State):
    print(f" {State[0]} | {State[1]} | {State[2]}")
    print(f"---|---|---")
    print(f" {State[3]} | {State[4]} | {State[5]}")
    print(f"---|---|---")
    print(f" {State[6]} | {State[7]} | {State[8]}")

def check_victory(State): 
    wins_possible=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins_possible:
        if (State[win[0]] == State[win[1]] == State[win[2]]=="X"):
            printBoard(State)
            print("X is the winner, Congratulations X your aura++ x 100 !!! :P ")
            return 1
        if(State[win[0]] == State[win[1]] == State[win[2]]=="O"):
            printBoard(State)
            print("O is the winner, Congratulations O your aura++ x 100 !!! :P ")
            return 0
        if all(isinstance(item, str) for item in State):
            printBoard(State)
            print("Game Tie")
            return -2
    return -1

if __name__=="__main__":
    State = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    turn = 1 # 1 for x and 0 for O
    print("Welcome to Tic Tac Toe")

    while(True):
        if turn==1:
            printBoard(State)
            print("X's chance")
            value = int(input("Enter the index: "))
            
            if State[value]!='O':
                State[value]='X'
            else:
                print("Enter a different value")
            
        if turn==0:
            printBoard(State)
            print("O's turn")
            value = int(input("Enter the index: "))
            
            if State[value]!='X':
                State[value]='O'
            else:
                print("Enter another index")
        
        c_victory=check_victory(State)

        if (c_victory!=-1):
            print("Game Over")
            break
        
        if (c_victory==-2):
            break

        turn = 1 if turn==0 else 0
