def multiplication(x, y):
    '''
    	5	6
    7	35	42
    8	40	48
    9	45	54
    10	50	60
    '''
    for column in y:
        print('\t', column, end='')
    print()

    for row in x:
        print(row, end='')
        for i in y:
            print('\t', i*row, end='')
        print()

