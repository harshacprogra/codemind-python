n = int(input())

fib_sequence = [0, 1]
while len(fib_sequence) < n:
    next_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_num)

print(*fib_sequence)
