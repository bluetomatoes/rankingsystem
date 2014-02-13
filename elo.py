<<<<<<< HEAD
class player:
    def __init__(self,name, elo):
        self.name = name
        self.elo = elo
file_adder = open("playerlist.txt", 'a')
def addplayer(newplayer):
    file_adder.write(newplayer + '\n')
    file_adder.flush()
player_list = []

file_searcher = open("playerlist.txt", 'r')
file = file_searcher.read()
print("Welcome to the foosball bot.\n [n] = add a player [g] = set up a game")

while True:
    inpuT = input()
    if inpuT == "n":
        newplayer_ = input("Please enter the name of the player")
        addplayer(newplayer_)
    if inpuT == "g":
        for i in range(1,5):
            player = input("please enter player number "+ str(i))
            checker = file.find(player)
            if checker != -1:
                print("Player successfully found.")
        #firstplayerteam1 = input("please enter the first player on Team 1")
        """checker = file.find(firstplayerteam1)
        if checker != -1:
            print("Player successfully found.")
            secondplayerteam1 = input("please enter the second player on Team 1")
            if checker != -1:
                print("Player successfully found.")
                
                if checker != -1:
                    print("Player successfully found.")
                    firstplayerteam2 = input("please enter the first player on Team 2")
                    checker = file.find(firstplayerteam2)
                    if checker != -1:
                        print("Player successfully found.")
                        secondplayerteam2 = input("please enter the second player on Team 2")
                    else:
                       print("Player not found. Please try again or add a new player to the database.") 
                else:
                    print("Player not found. Please try again or add a new player to the database.")
            else:
                print("Player not found. Please try again or add a new player to the database.")
        else:
            print("Player not found. Please try again or add a new player to the database.")"""
            
    if inpuT == "q":
        file_adder.close()
        break

new_list = []
for i in range (0,len(player_list)):
    new_list.append(player(player_list[i],1000))
class player:
    def __init__(self,name, elo):
        self.name = name
        self.elo = elo
player_file = open("playerlist.txt")
player_list = []
if input("Would you like to add a player to the list?(y/n)") == "y":
    newplayer = input("Please enter the name of the player")
    player_list.append(newplayer)
    print(player_list)
new_list = []
for i in range (0,len(player_list)):
    new_list.append(player(player_list[i],1000))
