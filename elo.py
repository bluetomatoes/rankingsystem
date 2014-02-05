class player:
    def __init__(self,name, elo):
        self.name = name
        self.elo = elo
player_file = open("playerlist")
player_list = []
if input("Would you like to add a player to the list?(y/n)") == "y":
    newplayer = input("Please enter the name of the player")
    player_list.append(newplayer)
    print(player_list)
new_list = []
for i in range (0,len(player_list)):
    new_list.append(player(player_list[i],1000))

