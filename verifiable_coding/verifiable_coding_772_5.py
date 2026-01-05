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
        # We'll use a dictionary to track the positions of each bit
        pos = {}
        for i in range(N):
            if S[i] == '1':
                if i+1 not in pos:
                    pos[i+1] = []
                pos[i+1].append(i+1)
        
        # For each position, check all possible exponential sequences starting from it
        for i in range(1, N+1):
            if S[i-1] == '1':
                # Start with i
                # Check all possible p > 1
                # We can only go up to N
                # For each p, check if i * p <= N
                # And if the bit at i * p is '1'
                # And so on
                # This is a BFS approach
                from collections import deque
                queue = deque()
                queue.append((i, [i]))
                
                while queue:
                    current, seq = queue.popleft()
                    if len(seq) >= 2:
                        # Check if the sequence is a palindrome
                        if seq == seq[::-1]:
                            count += 1
                    # Try to extend the sequence
                    for p in range(2, N//current + 1):
                        next_pos = current * p
                        if next_pos > N:
                            break
                        if S[next_pos-1] == '1':
                            new_seq = seq + [next_pos]
                            queue.append((next_pos, new_seq))
        
        print(count)

if __name__ == '__main__':
    solve()