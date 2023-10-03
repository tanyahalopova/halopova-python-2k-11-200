def max(*args):
    max_val = 0
    for arg in args:
        if arg > max_val:
            max_val = arg
    return max_val


print(max(4, 6, 2, 1, 9, 4, 6))
