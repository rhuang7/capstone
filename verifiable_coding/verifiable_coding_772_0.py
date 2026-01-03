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
        
        # Each single element is a valid sequence
        count += N
        
        # For each position i, check all possible p > 1 and see if the sequence can be extended
        for i in range(N):
            current = S[i]
            if current == '1':
                count += 1
                
            # Try all possible p > 1
            p = 2
            while True:
                next_pos = i * p
                if next_pos >= N:
                    break
                if S[next_pos] == current:
                    count += 1
                    # Check if we can extend further
                    next_next_pos = next_pos * p
                    if next_next_pos < N and S[next_next_pos] == current:
                        count += 1
                        # Continue extending
                        while True:
                            next_next_next_pos = next_next_pos * p
                            if next_next_next_pos >= N:
                                break
                            if S[next_next_next_pos] == current:
                                count += 1
                            else:
                                break
                            next_next_pos = next_next_next_pos
                else:
                    break
                p += 1
        
        print(count)

if __name__ == '__main__':
    solve()