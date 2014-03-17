#todo:
    #add elo functionality
    #add game history, winning streak boards
import time
class player:
    def __init__(self,name, elo):
        self.name = name
        self.elo = elo
file_adder = open("playerlist.txt", 'a')

game = []
winners =[]
losers = []
file_searcher = open("playerlist.txt", 'r')
playerfile = list(file_searcher)
playerfile = [line.rstrip('\n') for line in playerfile]
elofile = [line.split(' ,')[2] for line in playerfile]
playerfile = [line.split(' ,')[1] for line in playerfile]
player_scores = {}
print(elofile)

#for number items in playefile
    #player_scores[player] = playerfile[i]
for p in range(0,len(playerfile)):
    player = playerfile[p]
    player_scores[player] = elofile[p]
print(player_scores['Tom'])
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 2
def addplayer(newplayer, elo):
    playernum = file_len("playerlist.txt")
    file_adder.write(str(playernum) + ',' + newplayer + " ," + str(elo) + ', '+'\n')
    file_adder.flush()
def run():
    print("Welcome to the foosball bot.\n [n] = add a player [g] = set up a game")
run()
real_score = []
def score_checker():
    score_input = raw_input("Now tell me the score, in the form of x,y. X is the score of the first 2 players and y is the score of the second 2 players.")
    split_score = score_input.split(',')
    real_score.append(int(score_input.split(',')[0]))
    real_score.append(int(score_input.split(',')[1]))
def update_elo():
    
    pass
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
                        score_checker()
                        
                        if int(gametype_input) == 5:
                            print("5 received")
                            if real_score[0] > 5 or real_score[1] > 5:
                                print("Your score is too high. Don't try to trick me.")
                                del real_score[:]
                                score_checker()
                            elif real_score[0] < 0 or real_score[1] < 0:
                                print("Your score is too low. Do you even know what positive numbers are?")
                                del real_score[:]
                                score_checker()
                            else:
                                #always team 1 wins, never team2
                                if real_score[0] > real_score[1]:
                                    print("Game over. Good job to "+game[0]+" and " + game[1] + " for winning. Thanks for playing....\n")
                                    winners.append(game[0],game[1])
                                    losers.append(game[2],game[3])
                                elif real_score[0] < real_score[1]:
                                    print("Game over. Good job to "+game[2]+" and " + game[3] + " for winning. Thanks for playing....\n")
                                    winners.append(game[2],game[3])
                                    losers.append(game[0],game[1])
                                time.sleep(1)
                                del real_score[:]
                                del game[:]
                                print("Actually, I couldn't care less if you played.\n")
                                time.sleep(0.5)
                                run()
                        elif int(gametype_input) == 3:
                            print("gametype_received")
                            if real_score[0] > 3 or real_score[1] > 3:
                                print("Your score is too high. Don't try to trick me.")
                                del real_score[:]
                                score_checker()
                            elif real_score[0] < 0 or real_score[1] < 0:
                                print("Your score is too low. Do you even know what positive numbers are?")
                                del real_score[:]
                                score_checker()
                            else: 
                                del real_score[:]
                                print("Game over. Good job to "+game[0]+" and " + game[1] + " for winning. Thanks for playing....\n")
                                time.sleep(1)
                                del game[:]
                                print("Actually, I couldn't care less if you played.\n")
                                time.sleep(0.5)
                                run()                           
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
