def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1
        else:
            return x / 0 
    except ZeroDivisionError:
        return float('inf')  # Return infinity or handle the error as appropriate