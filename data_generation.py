from renjie_poker import RenjiePoker
import pandas as pd
import random

try:
    csv_df = pd.read_csv("renjie_poker_data.csv")
except:
    csv_df = pd.DataFrame(columns=["player_cards", "player_spades", "player_hearts", "player_clubs", "player_diamonds", "player_ranks", "player_straight", "dealer_cards", "dealer_spades", "dealer_hearts", "dealer_clubs", "dealer_diamonds", "dealer_ranks", "dealer_straight", "move", "win"])

# data_generator = RenjiePoker()
#csv_df = pd.DataFrame(columns=["player_cards", "player_spades", "player_hearts", "player_clubs", "player_diamonds", "player_ranks", "player_straight", "dealer_cards", "dealer_spades", "dealer_hearts", "dealer_clubs", "dealer_diamonds", "dealer_ranks", "dealer_straight", "move", "win"])
rows = []

num_runs = 10
num_moves = 1000
num_rows = 10000

for i in range(num_rows):
    print(i)
    # data = data_generator.simple_simulation_setup(1, True)
    # print(data)
    data_generator = RenjiePoker()
    data = data_generator.simple_simulation_setup(1, True)
    for j in range(num_moves):
        print(f"move: {j}")
        wins = 0
        move = [0]*52
        for k in range(52):
            r = random.random()
            if r > 0.5:
                if data[0][k] == 0 and data[7][k] == 0:
                    move[k] = 1
        for l in range(num_runs):
            # if l % 100 == 0:
            #     print(f"num_run: {l}")
            val = data_generator.simulation_move(move)
            if val == 1:
                print("win")
            wins += val

        
        row = {
            "player_cards": data[0],
            "player_spades": data[1],
            "player_hearts": data[2],
            "player_clubs": data[3],
            "player_diamonds": data[4],
            "player_ranks": data[5],
            "player_straight": data[6],
            "dealer_cards": data[7],
            "dealer_spades": data[8],
            "dealer_hearts": data[9],
            "dealer_clubs": data[10],
            "dealer_diamonds": data[11],
            "dealer_ranks": data[12],
            "dealer_straight": data[13],
            "move": move,
            "win": wins,
            "num_runs": num_runs
        }

        #print(row)

        df = pd.DataFrame([row])
        csv_df = pd.concat([csv_df, df])
        csv_df.to_csv("renjie_poker_data.csv", index=False)

# df = pd.DataFrame(rows)

# print(df)
# try:
#     csv_df = pd.concat([csv_df, df])
# except:
#     csv_df = df

# csv_df.to_csv("renjie_poker_data.csv", index=False)
