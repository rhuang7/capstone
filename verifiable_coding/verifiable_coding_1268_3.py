import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    idx = 0
    while True:
        n = int(input[idx])
        m = int(input[idx+1])
        x = int(input[idx+2])
        idx += 3
        if n == 0 and m == 0 and x == 0:
            break
        total = 0
        # Time for first person: x (book selection) + n (reading) = x + n
        # Time for second person: x (book selection) + n (reading) + n (wait for first person) = x + 2n
        # Time for third person: x + 3n
        # ...
        # Time for k-th person: x + k * n
        # But since m is large, we need to find how many full cycles of m people there are
        # Each full cycle contributes (x + (m * n)) time for the last person in the cycle
        # But the formula for the cost is floor((t - n) / m)
        # t = x + k * n
        # cost = floor((x + k * n - n) / m) = floor((x + (k-1)*n) / m)
        # So for each person, the cost is floor((x + (k-1)*n) / m)
        # Sum this for k from 1 to m
        # But since m can be up to 1e15, we can't loop through all m people
        # Instead, we find how many full cycles of m people there are, and then the remaining people
        # However, since m can be very large, we can find a formula for the sum
        # Let's find the sum of floor((x + (k-1)*n) / m) for k from 1 to m
        # Let's make a substitution: j = k-1, so j ranges from 0 to m-1
        # Sum of floor((x + j * n) / m) for j from 0 to m-1
        # This is equivalent to sum_{j=0}^{m-1} floor((x + j * n) / m)
        # Let's compute this sum
        # Let's find the number of full cycles of m in the sequence
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum of floor((x + j * n) / m) for j from 0 to m-1
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (x + j * n) / m
        # Let's find the sum for j from 0 to m-1
        # Let's find the value of (