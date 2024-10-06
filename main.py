def sum(a, b, c):
    return a+b+c
    
def printBoard(xState, zState):
    zero = 'X' if xState[0]==1 else ('O' if oState[0]==1 else 0)
    one = 'X' if xState[1]==1 else ('O' if oState[1]==1 else 1)
    two = 'X' if xState[2]==1 else ('O' if oState[2]==1 else 2)
    three = 'X' if xState[3]==1 else ('O' if oState[3]==1 else 3)
    four = 'X' if xState[4]==1 else ('O' if oState[4]==1 else 4)
    five = 'X' if xState[5]==1 else ('O' if oState[5]==1 else 5)
    six = 'X' if xState[6]==1 else ('O' if oState[6]==1 else 6)
    seven = 'X' if xState[7]==1 else ('O' if oState[7]==1 else 7)
    eight = 'X' if xState[8]==1 else ('O' if oState[8]==1 else 8)
    print(f" {zero} | {one} | {two}")
    print(f"---|---|---")
    print(f" {three} | {four} | {five}")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight}")

def check_victory(xState, oState): 
    wins_possible=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins_possible:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]])==3):
            printBoard(xState,oState)
            print("X is the winner, Congratulations X your aura++ x 100 !!! :P ")
            return 1
        if(oState[win[0]] + oState[win[1]] + oState[win[2]]==3):
            printBoard(xState,oState)
            print("O is the winner, Congratulations O your aura++ x 100 !!! :P ")
            return 0
    return -1

if __name__=="__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for x and 0 for O
    print("Welcome to Tic Tac Toe")
    
    while(True):
        printBoard(xState, oState)
        if turn==1:
            print("X's chance")
            value = int(input("Enter the index: "))
            xState[value] = 1
            
        else:
            print("O's turn")
            value = int(input("Enter the index: "))
            oState[value] = 1
        
        c_victory=check_victory(xState, oState)

        if (c_victory!=-1):
            print("Game Over")
            break

        turn = 1 if turn==0 else 0
