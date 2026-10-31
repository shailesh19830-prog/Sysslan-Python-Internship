def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        # Next number is the sum of the previous two
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

terms = 7
print(f"Fibonacci sequence for {terms} terms: {generate_fibonacci(terms)}")