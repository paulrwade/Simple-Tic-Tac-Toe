def render_game_board():
    print("---------")
    print("| " + grid_values[0] + " " + grid_values[1] + " " + grid_values[2] + " |")
    print("| " + grid_values[3] + " " + grid_values[4] + " " + grid_values[5] + " |")
    print("| " + grid_values[6] + " " + grid_values[7] + " " + grid_values[8] + " |")
    print("---------")
    return


def did_x_win():

    return(grid_values[0] + grid_values[1] + grid_values[2] == "XXX" or
           grid_values[3] + grid_values[4] + grid_values[5] == "XXX" or
           grid_values[6] + grid_values[7] + grid_values[8] == "XXX" or
           grid_values[0] + grid_values[3] + grid_values[6] == "XXX" or
           grid_values[1] + grid_values[4] + grid_values[7] == "XXX" or
           grid_values[2] + grid_values[5] + grid_values[8] == "XXX" or
           grid_values[0] + grid_values[4] + grid_values[8] == "XXX" or
           grid_values[2] + grid_values[4] + grid_values[6] == "XXX")


def did_o_win():

    return(grid_values[0] + grid_values[1] + grid_values[2] == "OOO" or
           grid_values[3] + grid_values[4] + grid_values[5] == "OOO" or
           grid_values[6] + grid_values[7] + grid_values[8] == "OOO" or
           grid_values[0] + grid_values[3] + grid_values[6] == "OOO" or
           grid_values[1] + grid_values[4] + grid_values[7] == "OOO" or
           grid_values[2] + grid_values[5] + grid_values[8] == "OOO" or
           grid_values[0] + grid_values[4] + grid_values[8] == "OOO" or
           grid_values[2] + grid_values[4] + grid_values[6] == "OOO")


def is_impossible_game():

    number_of_x = int(grid_values.count("X"))
    number_of_o = int(grid_values.count("O"))

    x_and_o_difference = abs(number_of_x - number_of_o)

    if x_and_o_difference > 1:

        return True

    elif did_x_win() and did_o_win():

        return True

    else:

        return False


def check_game_status():

    _status_message = ""

    if is_impossible_game():

        _status_message = "Impossible"

    else:

        if did_x_win():

            _status_message = "X wins"

        elif did_o_win():

            _status_message = "O wins"

        elif " " not in grid_values and "_" not in grid_values :

            _status_message = "Draw"

        else:

            _status_message = ""

    return _status_message


# Main Program Starts Here

grid_values = "         "

render_game_board()
turn_number = 0

while True:

    turn_number += 1

    while True:

        move_location = input().replace(" ", "")

        if not move_location.isnumeric():

            print("You should enter numbers!")

        else:

            move_location_row = int(move_location[0])
            move_location_col = int(move_location[1])

            if move_location_row > 3 or move_location_col > 3:

                print("Coordinates should be from 1 to 3!")

            else:

                move_character_position = ((move_location_row - 1) * 3) + (move_location_col - 1)

                if not grid_values[move_character_position] == " ":

                    print("This cell is occupied! Choose another one!")

                else:

                    if turn_number % 2 == 0:
                        character_to_insert = "O"
                    else:
                        character_to_insert = "X"

                    grid_values = (grid_values[:move_character_position] + character_to_insert +
                                   grid_values[move_character_position + 1:])

                    break

    render_game_board()

    game_status = check_game_status()

    if game_status != "":

        print(game_status)

        break
