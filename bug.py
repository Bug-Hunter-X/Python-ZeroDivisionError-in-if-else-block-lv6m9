def function_with_uncommon_error(x):
    if x == 0:
        return 1
    else:
        return x / 0  # ZeroDivisionError