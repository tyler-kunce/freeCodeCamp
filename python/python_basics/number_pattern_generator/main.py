def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    num_pattern = ''
    for i in range(1, n+1):
        if i < n:
            num_pattern += str(i) + ' '
        if i == n:
            num_pattern += str(i)
    return num_pattern

print(number_pattern(4))