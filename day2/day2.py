    f.close()
# A =   Rock   = X
# B =  Paper   = Y
# C = Scissors = Z

res_map = {"A A": 4,
           "A B": 8,
           "A C": 3,
           "B A": 1,
           "B B": 5,
           "B C": 9,
           "C A": 7,
           "C B": 2,
           "C C": 6}

mod_map = {"A": 0,
           "B": 1,
           "C": 2}
game_map = {value:key for key, value in mod_map.items()}

new_game = []
for g in games:
    opp_move = g[0]
    result = g[2]
    if result == "X":
        my_move = game_map[(mod_map[opp_move] + 2)%3]
    elif result == "Z":
        my_move = game_map[(mod_map[opp_move] + 1)%3]
    else:
        my_move = opp_move
    new_game.append(opp_move + " " + my_move)
print(sum([res_map[g] for g in new_game]))
