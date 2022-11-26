import game_2048

if __name__ == '__main__':
    # calling start_game() function to initialize the matrix
    grid = game_2048.start_game()

while True:
    # take the user input
    try:
        x = input("Press the command: ")
        if not x.isalpha():
            raise TypeError
        if x not in ('w','a','s','d'):
            raise ValueError
    except TypeError:
        print('Please only enter letters not numbers. Try again')
    except ValueError:
        print('Please only enter \'w,a,s,d\'.Try again.')

    if x == 'w':
        # call the move up function
        grid, changed = game_2048.move_up(grid)

        # get the current state and print it
        res = game_2048.get_state(grid)
        print(res)

        if res == 'Game Continue':
            game_2048.get_new_2(grid)

        # else break the loop and continue to press the command
        else:
            break

    elif x == 'a':
        grid, changed = game_2048.move_left(grid)
        res = game_2048.get_state(grid)
        print(res)
        if res == 'Game Continue':
            game_2048.get_new_2(grid)
        else:
            break


    elif x == 's':
        grid, changed = game_2048.move_down(grid)
        res = game_2048.get_state(grid)
        print(res)
        if res == 'Game Continue':
            game_2048.get_new_2(grid)
        else:
            break

    elif x == 'd':
        grid, changed = game_2048.move_right(grid)
        res = game_2048.get_state(grid)
        print(res)
        if res == 'Game Continue':
            game_2048.get_new_2(grid)
        else:
            break

    # print each matrix after each move
    print(grid)
