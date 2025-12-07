

def fibonacci_sequence(start , end , number ):

    if number < 0:
        return []
    elif number == 0:
        return [start]
    elif number == 1:
        return [start, end]
    else:
        seq = [start, end]
        for i in range(2, number + 1):
            next_value = seq[i - 1] + seq[i - 2]
            seq.append(next_value)
        return seq


print(fibonacci_sequence(0, 1, 10))