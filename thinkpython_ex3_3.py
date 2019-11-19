def make_grid():
    start_plus = '+ - - - - + - - - - +\n'
    start_pipe = '|         |         |\n'
    print(2* (start_plus + 4 * start_pipe) + start_plus, end=' ')
    

# make_grid()

def four_grid():
    start_plus = '+ - - - - + - - - - + - - - - + - - - - +\n'
    start_pipe = '|         |         |         |         |\n'
    print(4* (start_plus + 4 * start_pipe) + start_plus, end=' ')

four_grid()