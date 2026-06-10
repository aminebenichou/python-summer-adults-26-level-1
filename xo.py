cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = "X"
while True:
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("___|___|___")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("___|___|___")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")

    user_input = input("Enter a number 1-9: ")
    i=0
    while i<len(cells):
        if user_input==str(cells[i]):
            cells[i]=player
            if player=="X":
                player="O"
            else:
                player="X"
        
        i = i+1