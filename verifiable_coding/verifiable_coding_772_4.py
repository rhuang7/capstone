import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        N = len(S)
        count = 0
        
        # Single element sequences
        count += N
        
        # For each possible starting position i
        for i in range(N):
            # For each possible p > 1
            p = 2
            j = i + 1
            while j < N:
                # Check if the sequence is exponential
                # i, j, j*p, j*p*p, ...
                # We need to check if the sequence forms a palindrome
                # We can only go up to N
                # We'll check for each step
                # Start with the sequence [i]
                # Then add j = i*p
                # Then add j*p, etc.
                # We'll check for each possible sequence
                # We'll use a set to track the positions in the sequence
                # We'll check if the sequence is a palindrome
                # We'll do this recursively
                # But for efficiency, we'll do it iteratively
                # We'll track the current sequence
                seq = [i]
                current = i
                while True:
                    next_pos = current * p
                    if next_pos >= N:
                        break
                    seq.append(next_pos)
                    current = next_pos
                # Check if the sequence is a palindrome
                if seq == seq[::-1]:
                    count += 1
                # Try next p
                p += 1
                j = i + 1
        print(count)

if __name__ == '__main__':
    solve()