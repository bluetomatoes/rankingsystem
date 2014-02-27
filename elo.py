#todo:
    #add [s] functionality
import time
class player:
    def __init__(self,name, elo):
        self.name = name
        self.elo = elo
file_adder = open("playerlist.txt", 'a')
def addplayer(newplayer, elo):
    file_adder.write(newplayer + " , " + str(elo) + ',' + '\n')
    file_adder.flush()
game = []
file_searcher = open("playerlist.txt", 'r')
playerfile = list(file_searcher)
playerfile = [line.rstrip('\n') for line in playerfile]
playerfile = [line.split(' ,')[0] for line in playerfile]

print(playerfile)
def run():
    print("Welcome to the foosball bot.\n [n] = add a player [g] = set up a game")
run()

while True:
    inpuT = raw_input()
    if inpuT == "n":
        newplayer_ = raw_input("Please enter the name of the player")
        addplayer(newplayer_, 1000)
        playerfile.append(newplayer_)
        print("In case you were too stupid to remember the person you just entered into our \n database, the new playerfile is \n" + str(playerfile))
    elif inpuT == 'g':
        i = 1
        while i < 5:
            print(i)
            player = raw_input("please enter player number "+ str(i))
            if player in playerfile:
                print("Player successfully found. Thanks for being able to spell.")
                if player not in game:
                    game.append(player)
                elif player in game:
                    print("This player has already been entered, dumb***. Are you trying to boost your own ranking or are you just being stupid?")
                    i-=1
            else:
                print("Player not found. Please try again with good spelling or add a new player to the database.")
                i-=1
            if i == 4:
                print("The team is ", game)
                time.sleep(1)
                print("LET THE GAMES BEGIN!!!! Press [c] to cancel.")
                game_on = True
                while i == 4:
                    ingame_input = raw_input("The game is in progress. \n [s] = enter the score [c] = cancel game")
                    if ingame_input == 's':
                        i=5
                        gametype_input = raw_input("What type of game? [3/5]")
                        if gametype_input == '3':
                            score_input = raw_input("Now tell me the score, in the form of x,y. X is the score of the first 2 players and y is the score of the second 2 players.")
                            score_input.split(',')
                            print(score_input)
                    if ingame_input == 'c':
                        del game[:]
                        print("\nGame canceled. Why the F**K did you set it up in the first place?\n")
                        i = 5
                        time.sleep(0.5)
                        run()
                        
            i+=1
        #firstplayerteam1 = input("please enter the first player on Team 1")

    elif inpuT == "q":
        file_adder.close()
        break
