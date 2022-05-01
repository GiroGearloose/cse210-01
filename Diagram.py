# Code of Tic Tac Toe game 
# Version by Paulo Lopes
# CSE 210 Brother Carter

def main():
    gamer = other_gamer("")
    screen = create_screen()
    while not (winner(screen) or my_print(screen)):
        show_screen(screen)
        make_move(gamer, screen)
        gamer = other_gamer(gamer)
    show_screen(screen)
    print("Weel Done. Try again and Good Luck!") 

def create_screen():
    screen = []
    for square in range(9):
        screen.append(square + 1)
    return screen

def show_screen(screen):
    print()
    print(f"{screen[0]}|{screen[1]}|{screen[2]}")
    print('-+-+-')
    print(f"{screen[3]}|{screen[4]}|{screen[5]}")
    print('-+-+-')
    print(f"{screen[6]}|{screen[7]}|{screen[8]}")
    print()
    
def my_print(screen):
    for square in range(9):
        if screen[square] != "x" and screen[square] != "o":
            return False
    return True 
    
def winner(screen):
    return (screen[0] == screen[1] == screen[2] or
            screen[3] == screen[4] == screen[5] or
            screen[6] == screen[7] == screen[8] or
            screen[0] == screen[3] == screen[6] or
            screen[1] == screen[4] == screen[7] or       
            screen[2] == screen[5] == screen[8] or
            screen[0] == screen[4] == screen[8] or
            screen[2] == screen[4] == screen[6])
            
            
def make_move(gamer, screen):
    square = int(input(f"{gamer} please your turn choose square (1-9): "))
    screen[square - 1] = gamer

def other_gamer(actual):
    if actual == "" or actual == "o":
        return "x"
    elif actual == "x":
        return "o"

if __name__ == "__main__":
    main()
