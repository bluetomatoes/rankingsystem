class player:
    def __init__(self,name, elo):
        self.name = name
        self.elo = elo
file_adder = open("playerlist.txt", 'a')
def addplayer(newplayer):
    #player_ = player(newplayer, 1000)
    file_adder.write(newplayer + '\n')
    file_adder.flush()
game = []
file_searcher = open("playerlist.txt", 'r')
playerfile = list(file_searcher)
playerfile = [line.rstrip('\n') for line in playerfile]
print(playerfile)
print("Welcome to the foosball bot.\n [n] = add a player [g] = set up a game")
while True:
    inpuT = raw_input()
    if inpuT == "n":
        newplayer_ = raw_input("Please enter the name of the player")
        addplayer(newplayer_)
        playerfile.append(newplayer_)
        print("In case you were too stupid to remember the person you just entered into our \n database, the new playerfile is \n" + str(playerfile))
    elif inpuT == 'g':
        i=1
        while i < 5:
            player = raw_input("please enter player number "+ str(i))
            if player in playerfile:
                print("Player successfully found.")
                game.append(player)
            else:
                print("Player not found. Please try again or add a new player to the database.")
                i-=1
            if i == 4:
                print("The team is ", game)
            i+=1
        #firstplayerteam1 = input("please enter the first player on Team 1")

    if inpuT == "q":

        file_adder.close()
        break
