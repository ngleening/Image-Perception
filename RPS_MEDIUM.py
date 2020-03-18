import random

computer_choice = {0: "R", 1: "P", 2: "S"}


# Basic Play

def play_basic(human_input, com_select):
    """
    This function plays using a simple psych. concept on how humans would play.
    It does not account for the number of times the human player plays his/her gesture
    """
    outcome = ()
    if human_input == "R":
        if com_select == "P":
            fut_com_select = "S"
            outcome = ("C", human_input, com_select, fut_com_select)

        elif com_select == "S":
            fut_com_select = "P"
            outcome = ("H", human_input, com_select, fut_com_select)

    elif human_input == "P":
        if com_select == "S":
            fut_com_select = "R"
            outcome = ("C", human_input, com_select, fut_com_select)

        elif com_select == "R":
            fut_com_select = "S"
            outcome = ("H", human_input, com_select, fut_com_select)

    elif human_input == "S":
        if com_select == "R":
            fut_com_select = "P"
            outcome = ("C", human_input, com_select, fut_com_select)

        elif com_select == "P":
            fut_com_select = "R"
            outcome = ("H", human_input, com_select, fut_com_select)

    if len(outcome) != 0:
        return outcome

    fut_com_select = computer_choice[random.randint(0, 2)]
    return "D", human_input, com_select, fut_com_select


def pattern_analyzer(human_choice_arr, computer_choice_arr):
    """
    This function will be activated once the user plays more than 4 round of RPS. It plays
    in a probabilistic manner looking for pairs or triplets.

    This function also has another feature which is to catch user that tries to play the
    computer's previous move & whether the human plays in the pattern to beat the previous
    move made by the computer
    """

    win_moves = {"R": "P",
                 "P": "S",
                 "S": "R"}

    if len(human_choice_arr) > 5:
        # Analyse if human is trying to copy computer's previous move. There is a catch, human must copy
        # 3 consecutive moves for computer to detect
        prev_com_five_moves = computer_choice_arr[-5:]
        prev_human_four_moves = human_choice_arr[-4:]
        if prev_com_five_moves[0:3] == prev_human_four_moves[0:3]:
            return "copycat", prev_com_five_moves[0:3]

    if len(human_choice_arr) > 5:
        # Analyse if human is just trying to use a move to beat the computer's previous move. This must
        # be over 4 moves at least
        prev_com_five_moves = computer_choice_arr[-5:]
        prev_com_four = prev_com_five_moves[0:4]
        prev_human_four_moves = human_choice_arr[-4:]

        count = 0
        for i in range(len(prev_com_four)):
            pred = win_moves[prev_com_four[i]]
            if pred == prev_human_four_moves[i]:
                count += 1
        if count == 4:
            return "rat", "TEST"

    # Get previous 6 moves to detect triplets
    if len(human_choice_arr) > 5:
        prev_six_moves = human_choice_arr[-6:]

        # Analyse if there's triplets repeats, compare if first 3 are the same as the next 3
        first_triplet = prev_six_moves[0] + prev_six_moves[1] + prev_six_moves[2]
        next_triplet = prev_six_moves[3] + prev_six_moves[4] + prev_six_moves[5]
        if first_triplet == next_triplet:
            return "triplet", first_triplet

            # Get previous 4 moves to detect pairs
    if len(human_choice_arr) > 3:
        prev_human_four_moves = human_choice_arr[-4:]
        # Analyse if there's pair repeats, compare if first 2 pairs are the same as the next 2 pairs
        first_pair = prev_human_four_moves[0] + prev_human_four_moves[1]
        second_pair = prev_human_four_moves[2] + prev_human_four_moves[3]
        if first_pair == second_pair:
            pair_combi = first_pair
            return "pairs", pair_combi

    return False


def play_pattern(pattern, rnd):
    """
    This function will play in the opposite way of the identified pattern.
    """
    # Get computer to select the winning choice
    if pattern[rnd] == "R":
        return "P"
    elif pattern[rnd] == "P":
        return "S"
    elif pattern[rnd] == "S":
        return "R"


def play_copycat(computer_choice_arr):
    """
    Look at the last choice made by computer and do a winning move against
    the last move made by the computer
    """
    if computer_choice_arr[-1] == "S":
        return "R"
    elif computer_choice_arr[-1] == "P":
        return "S"
    elif computer_choice_arr[-1] == "R":
        return "P"


def play_rat(computer_choice_arr):
    """
    Look at the last choice the computer made
    """
    last_move = computer_choice_arr[-1]
    if last_move == "R":
        return "S"
    elif last_move == "P":
        return "R"
    elif last_move == "S":
        return "P"


def pattern_player_outcome(human_input, com_select):
    outcome = ()
    if human_input == "R":
        if com_select == "P":
            outcome = ("C", human_input, com_select)

        elif com_select == "S":
            outcome = ("H", human_input, com_select)

    elif human_input == "P":
        if com_select == "S":
            outcome = ("C", human_input, com_select)

        elif com_select == "R":
            outcome = ("H", human_input, com_select)

    elif human_input == "S":
        if com_select == "R":
            outcome = ("C", human_input, com_select)

        elif com_select == "P":
            outcome = ("H", human_input, com_select)

    if len(outcome) != 0:
        return outcome
    return "D", human_input, com_select


def remove_cheats(human_choice_arr, num_cheats):
    if len(human_choice_arr) > 3:
        end = len(human_choice_arr) - num_cheats
        new_human_choice_arr = human_choice_arr[0:end]
        return new_human_choice_arr
    return human_choice_arr


# Computer Selection
def computer_selects(human_choice):
    """
    The computer will select base on prior probability made by user and make a counter measure
    """
    if human_choice == "R":
        return "P"

    if human_choice == "P":
        return "S"

    if human_choice == "S":
        return "R"


def get_probability_table(human_choice_arr):
    """
    This function analyses the pattern of human behaviour if a human plays by instincts instead
    of having a huge memory to store all his/her outputs and the computer's ones too.

    This function will try to play by an MDP/Q-learning policy. It will need at least 10 inputs
    before it can be created.
    """

    # Instantiate number of times pairs are thrown table
    pairs_dictionary = {"R": {"R": 0, "S": 0, "P": 0},
                        "S": {"R": 0, "S": 0, "P": 0},
                        "P": {"R": 0, "S": 0, "P": 0}}

    # Create probability table
    probability_dictionary = {"R": {"R": 0, "S": 0, "P": 0},
                              "S": {"R": 0, "S": 0, "P": 0},
                              "P": {"R": 0, "S": 0, "P": 0}}

    # Get probability of pairs occuring together
    if len(human_choice_arr) >= 10:
        for i in range(len(human_choice_arr) - 1):
            # 1st key - human's prev choice
            sub_dictionary = pairs_dictionary[human_choice_arr[i]]
            # 2nd key - human's curr choice
            sub_dictionary[human_choice_arr[i + 1]] += 1

        # Update probaility table
        for a_key in probability_dictionary:
            sub_probability_dictionary = probability_dictionary[a_key]
            retrieved_dictionary = pairs_dictionary[a_key]
            for a_sub_key in sub_probability_dictionary:
                value = retrieved_dictionary[a_sub_key]
                update_value = value / len(human_choice_arr)
                sub_probability_dictionary[a_sub_key] = update_value

        return probability_dictionary
    return ""


def get_probability(human_choice_arr, computer_choice_arr):
    """
    This function gets the probability of what the human played vs what the computer played.
    It returns a probability table of what human and computer played.
    """

    # Declare table showing number of times com, human played
    played_times_dictionary = {"R": {"R": 0, "S": 0, "P": 0},
                               "S": {"R": 0, "S": 0, "P": 0},
                               "P": {"R": 0, "S": 0, "P": 0}}

    probability_dictionary = {"R": {"R": 0, "S": 0, "P": 0},
                              "S": {"R": 0, "S": 0, "P": 0},
                              "P": {"R": 0, "S": 0, "P": 0}}

    # Update number table
    if len(human_choice_arr) >= 10:
        for i in range(len(human_choice_arr)):
            human_choice = human_choice_arr[i]
            com_choice = computer_choice_arr[i]

            played_times_dictionary[com_choice][human_choice] += 1

        for a_key in played_times_dictionary:
            sub_dictionary = probability_dictionary[a_key]
            for sub_key in sub_dictionary:
                prob_value = played_times_dictionary[a_key][sub_key] / len(human_choice_arr)
                sub_dictionary[sub_key] = prob_value
        return probability_dictionary
    return ""


def get_rewards_table(human_choice_arr, computer_choice_arr):
    # Declare rewards table rule
    rule = {"R": {"R": 0.5, "P": -1, "S": 1.5},
            "S": {"R": -1, "P": 1.5, "S": 0.5},
            "P": {"R": 1.5, "P": 0.5, "S": -1}}

    # Create rewarded table 
    rewards_table = {"R": {"R": 0, "S": 0, "P": 0},
                     "S": {"R": 0, "S": 0, "P": 0},
                     "P": {"R": 0, "S": 0, "P": 0}}

    for i in range(len(human_choice_arr)):
        human_choice = human_choice_arr[i]
        com_choice = computer_choice_arr[i]

        reward = rule[com_choice][human_choice]
        rewards_table[com_choice][human_choice] += reward

    return rewards_table


def get_prob_rewards_table(rewards_table, probability_dictionary):
    """
    This function returns the probability-rewards table
    """

    # Declare prob_rewards table
    prob_rewards_table = {"R": {"R": 0, "S": 0, "P": 0},
                          "S": {"R": 0, "S": 0, "P": 0},
                          "P": {"R": 0, "S": 0, "P": 0}}

    for a_key in prob_rewards_table:
        sub_dictionary = prob_rewards_table[a_key]
        for a_sub_key in sub_dictionary:
            # Pick up rewards
            r = rewards_table[a_key][a_sub_key]
            # Pick up probability
            p = probability_dictionary[a_key][a_sub_key]
            # Update
            sub_dictionary[a_sub_key] = r * p

    return prob_rewards_table


def play_by_probability(human_choice_arr, prob_rewards_table):
    """
    This function tries to use a move that should give the highest possible reward
    """
    # Get probability of next move by human
    human_moves = get_probability_table(human_choice_arr)
    human_next_move_probability = human_moves[human_choice_arr[-1]]

    env_error_count = 0
    for move_key in human_next_move_probability:
        if human_next_move_probability[move_key] == 0.0:
            env_error_count += 1

    if env_error_count != 3:
        # Retrieve highest value from prob_rewards_table
        highest_prob_value = 0
        predicted_move = ""
        for a_key in human_next_move_probability:
            if human_next_move_probability[a_key] > highest_prob_value:
                highest_prob_value = human_next_move_probability[a_key]
                predicted_move = a_key

        # print("PREDICTED MOVE:",predicted_move)
        # Find the corresponding reward which is the highest
        rp_table_sub_key = predicted_move
        highest_rp_value = -20
        com_move = ""
        for rp_key in prob_rewards_table:
            if prob_rewards_table[rp_key][rp_table_sub_key] > highest_rp_value:
                highest_rp_value = prob_rewards_table[rp_key][rp_table_sub_key]
                com_move = rp_key

        return com_move
    return "Cannot Retrieve Probability"


### ======================= JUST TO SEE STATISTIC ================================= ###
# Get probability
def get_prob(human_choice_arr):
    """
    Returns the probability of human making a choice on the move/gesture he wants
    """
    num_R = human_choice_arr.count("R")
    num_S = human_choice_arr.count("S")
    num_P = human_choice_arr.count("P")

    prob_R = num_R / len(human_choice_arr)
    prob_S = num_S / len(human_choice_arr)
    prob_P = num_P / len(human_choice_arr)

    return {"R": prob_R, "S": prob_S, "P": prob_P}


def get_com_prob(computer_choice_arr):
    """
    Finds the probability of the computer playing the gestures. Returned in dictionary format.
    What we try to prove here is that selection of RPS is not just an equal 1/3 chance each time 
    for human and computer.
    """
    num_com_R = computer_choice_arr.count("R")
    num_com_P = computer_choice_arr.count("P")
    num_com_S = computer_choice_arr.count("S")

    prob_com_R = num_com_R / len(computer_choice_arr)
    prob_com_P = num_com_P / len(computer_choice_arr)
    prob_com_S = num_com_S / len(computer_choice_arr)

    return {"R": prob_com_R, "S": prob_com_P, "P": prob_com_S}


## Play the game

def play_game(human_choice_arr, computer_choice_arr):
    if len(human_choice_arr) == 0:
        com_select = computer_choice[random.randint(0, 1)]
        return com_select

    # Check for pattern
    if len(human_choice_arr) >= 4 and pattern_analyzer(human_choice_arr, computer_choice_arr) != False:

        # Retrieve pattern
        predicted_pattern = pattern_analyzer(human_choice_arr, computer_choice_arr)[0]

        if predicted_pattern == "triplet":
            com_select = play_pattern(pattern_analyzer(human_choice_arr, computer_choice_arr)[1], 0)

        elif predicted_pattern == "pairs":
            com_select = play_pattern(pattern_analyzer(human_choice_arr, computer_choice_arr)[1], 0)

        elif predicted_pattern == "copycat":
            com_select = play_copycat(computer_choice_arr)

        elif predicted_pattern == "rat":
            com_select = play_rat(computer_choice_arr)

        return com_select

    # If no pattern detected, and less than 10 rounds of play, play a basic manner
    elif len(human_choice_arr) < 9 and pattern_analyzer(human_choice_arr, computer_choice_arr) == False:
        # Basic game play will be chosen ==> E.g: "D", human_input, com_select, fut_com_select
        game_outcome_basic = play_basic(human_choice_arr[-1], computer_choice_arr[-1])
        com_select = game_outcome_basic[3]  # Computer makes a future selection
        return com_select

    # If number of rounds played >= 10
    else:

        # Play by probability distribution
        com_prob_select = ""
        if get_probability(human_choice_arr, computer_choice_arr) != "":

            probability_dictionary = get_probability(human_choice_arr, computer_choice_arr)
            rewards_table = get_rewards_table(human_choice_arr, computer_choice_arr)
            prob_rewards_table = get_prob_rewards_table(rewards_table, probability_dictionary)

            if play_by_probability(human_choice_arr, prob_rewards_table) != "Cannot Retrieve Probability":
                com_prob_select = play_by_probability(human_choice_arr, prob_rewards_table)
            else:
                com_prob_select == ""

        if com_prob_select != "":
            com_select = com_prob_select

        else:
            prob_dictionary = get_prob(human_choice_arr)
            highest_val = 0

            for key in prob_dictionary:
                if prob_dictionary[key] > highest_val:
                    highest_val = prob_dictionary[key]
                    human_choice = key
            com_select = computer_selects(human_choice)

        return com_select
