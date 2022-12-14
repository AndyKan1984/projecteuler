def problem2(max_int):
    first = 1
    second = 2
    sum_event = 0
    while (second < max_int):
        if (second % 2 == 0):
            sum_event += second
        next_fib = first+second
        first = second
        second = next_fib

    return sum_event
