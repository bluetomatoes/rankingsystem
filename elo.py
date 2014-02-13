#fix: putting in "t" and getting a player
class player:
    def __init__(self,name, elo):
        self.name = name
        self.elo = elo
file_adder = open("playerlist.txt", 'a')
def addplayer(newplayer):
    #player_ = player(newplayer, 1000)
    #file_adder.write(player_ + '\n')
    file_adder.flush()
game = []
file_searcher = open("playerlist.txt", 'r')
cleaner = open('playerlist.txt').read().replace('\n', '')
file = list(file_searcher)

player_list = file
file = [line.rstrip('\n') for line in file]
print(file)

print("Welcome to the foosball bot.\n [n] = add a player [g] = set up a game")

while True:
    playerinput = raw_input()
    if playerinput == 'n':
        #newplayer_ = input("Please enter the name of the player")
        #addplayer(newplayer_)
        print("debug")
    elif playerinput == 'g':
        i=1
        while i < 5:
            player = raw_input("please enter player number "+ str(i))
            checker = file.find(player)
            if checker != -1:
                print("Player successfully found.")
                game.append(player)
                if i ==4:
                    print("players of the game are:",game)
            else:
                print("Player not found. Please try again or add a new player to the database.")
                i = i-1
            i+=1
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
            
    if playerinput == "q":
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

cleaner.close()
