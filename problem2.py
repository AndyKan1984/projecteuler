def sum_evens_in_fibonacci(max_int):
    first = 1
    second = 2
    sum_evens = 0
    while (second < max_int):
        if (second % 2 == 0):
            sum_evens += second
        next_fib = first+second
        first = second
        second = next_fib

    return sum_evens
