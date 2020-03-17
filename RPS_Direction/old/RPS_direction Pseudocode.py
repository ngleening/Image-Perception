def RPS(user_input, computer_input):
    # if...

    # return (False, 'draw') (True, 'user') (True, 'cpu')

def direction(user_input, computer_input):
    # if same return True
    # else False


RPS_draw = False
RPS_winner = None
direction_winner_found = False
while not direction_winner_found:

    while not RPS_draw:
        # Detect the user's input
        # Generate a compute_input
        RPS_draw, RPS_winner = RPS(user_input, computer_input)
        # break out if not draw

    direction_winner_found = direction(RPS_winner)

print(f"Winner found: {RPS_winner}")
    