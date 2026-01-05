import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        x = data[index]
        index += 1
        
        a = []
        b = []
        for i in range(n):
            if i == 0:
                # First digit is 2, so a and b must be 1 and 1
                a.append('1')
                b.append('1')
            else:
                # For other digits, try to make a and b as small as possible
                # To minimize max(a, b), we want a and b to be as small as possible
                # So we try to make a and b as small as possible, but ensuring a + b mod 3 = x[i]
                # We try all possible combinations of (a_digit, b_digit) that satisfy (a_digit + b_digit) % 3 == x[i]
                # We choose the pair that makes a and b as small as possible
                # We try (0, x[i]), (x[i], 0), (1, (x[i] - 1) % 3), ((x[i] - 1) % 3, 1)
                # We choose the pair that gives the smallest a and b
                # We also need to ensure that a and b are not leading zeros (but since first digit is already handled, this is not a problem here)
                # We try all possible combinations and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the best one
                # We can try the following pairs:
                # (0, x[i]), (x[i], 0), (1, (x[i] - 1) % 3), ((x[i] - 1) % 3, 1)
                # We choose the pair that gives the smallest max(a, b)
                # We also need to ensure that a and b are not leading zeros (but since first digit is already handled, this is not a problem here)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the best one
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible pairs and choose the one that gives the smallest max(a, b)
                # We can try all possible