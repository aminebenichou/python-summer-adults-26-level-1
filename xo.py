cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = "X"
resetable = False
while True:
    n=0
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("___|___|___")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("___|___|___")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    if resetable:
        if input("Click R to reset the game") == "r":
                    cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    player = "X"

    user_input = input("Enter a number 1-9: ")
    i=0
    while i<len(cells):
        if user_input==str(cells[i]):
            cells[i]=player
            if player=="X":
                player="O"
            else:
                player="X"
        
        if type(cells[i])!=int:
            n += 1
            print(n)

        if n==9:
            resetable = True

            
        
        i = i+1
    
