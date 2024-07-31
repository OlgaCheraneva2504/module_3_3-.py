def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['good', [False, 16, 987], 175]
values_dict = {'a': ['home', 54, 222], 'b': 16, 'c': 'Olya'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [35, 'one']
print_params(*values_list_2, 42)

