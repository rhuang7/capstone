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
        
        # Each single element is an exponential sequence and a palindrome
        count += N
        
        # For each possible starting index i
        for i in range(N):
            # For each possible p > 1
            p = 2
            current = i + 1
            while current < N:
                # Check if the sequence is a palindrome
                # The sequence is [i+1, current]
                if S[i] == S[current - 1]:
                    count += 1
                # Move to next element in the exponential sequence
                current *= p
        
        print(count)

if __name__ == '__main__':
    solve()