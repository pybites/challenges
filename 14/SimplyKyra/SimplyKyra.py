from functools import wraps


def sum_numbers(func):
    '''Decorator to find the sum of each dict value and add it to the beginning of the list'''
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        for key, values in args[0].items():
            args[0][key].insert(0, sum(values))
        return func(*args, **kwargs)
    return wrapper


def pretty_table_header(func):
    '''Decorator to add a heading to the table'''
    def wrapper(*args, **kwargs):
        columns = args[len(args)-1]
        value = "".join(["\tHeader " + str(i+1) for i in range(0, columns)])
        print(f"Name\t\tSum\t{value}")
        return func(*args, **kwargs)
    return wrapper


@pretty_table_header
@sum_numbers
def print_a_dict(a_dict, columns):
    for key, values in a_dict.items():
        my_str = f"{key}"
        first = 1
        for num in values:
            if first < 3:
                first += 1
                my_str = my_str + "\t\t" + str(num)
            else:
                my_str = my_str + "\t\t\t" + str(num)
        print(my_str)


if __name__ == '__main__':
    ''' Creating a dict with key short name and values a list of five digits the two decorators make it look pretty '''
    my_numbers = {"row1": [43,54,2,3,45],
                  "row2": [32,34,5,32,3],
                  "named": [3,4,5,2,34]}
    print_a_dict(my_numbers, 5)



