# Author: Paulo Sergio Lopes
# TIC-TAC-TOE game code.
# Working on Github

def game_screen():
    
   print("1|2|3") 
   print("-+-+-")
   print("4|5|6") 
   print("-+-+-")
   print("7|8|9") 
   print("-+-+-")

def search_replace():
    print()
    
def play():
    player = input("player 1 type X player 2 type O: ")
    Choicest_number = input("Type your choicest number from 1 to 9: ")
    if player.upper() == "X":
     search_replace()
    elif player.upper() == "O":
     search_replace() 
    else:
     print("aqui")
   
print("You can play TiC-TaC-Toe")
choice = input("to Play type Y and to quit type N: ")

if choice.upper() == "Y":  
    game_screen()
    play()
else:
    print("OK see you later")