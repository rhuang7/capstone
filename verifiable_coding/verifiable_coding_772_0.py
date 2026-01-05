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
            # For each possible p (multiplication factor)
            p = 2
            while True:
                next_pos = i * p
                if next_pos >= N:
                    break
                # Check if the sequence is a palindrome
                # We need to check if the sequence from i to next_pos is a palindrome
                # Since it's exponential, it's i, i*p, i*p^2, ...
                # So we need to check the sequence S[i], S[i*p], S[i*p^2], ...
                # But since we're only checking two elements for now, we can check if S[i] == S[next_pos]
                if S[i] == S[next_pos]:
                    count += 1
                p += 1
        
        print(count)

if __name__ == '__main__':
    solve()