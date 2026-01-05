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
        
        # Exponential sequences of length >= 2
        # We'll use a dictionary to track positions for each value
        from collections import defaultdict
        pos = defaultdict(list)
        for i in range(N):
            pos[S[i]].append(i + 1)  # 1-based indexing
        
        # For each possible starting position
        for i in range(1, N + 1):
            # Check all possible p > 1
            p = 2
            while True:
                next_pos = i * p
                if next_pos > N:
                    break
                # Check if the next position is in the string
                if next_pos <= N:
                    # Check if the sequence [i, next_pos] is a palindrome
                    if S[i - 1] == S[next_pos - 1]:
                        count += 1
                p += 1
        
        print(count)

if __name__ == '__main__':
    solve()