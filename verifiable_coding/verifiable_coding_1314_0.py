import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N
    results = []
    for _ in range(M):
        C = data[idx]
        idx += 1
        K = int(data[idx])
        idx += 1
        X = data[idx]
        idx += 1
        
        # Generate all non-empty continuous subarrays and replace with max
        max_values = []
        for i in range(N):
            current_max = A[i]
            for j in range(i, N):
                current_max = max(current_max, A[j])
                max_values.append(current_max)
        
        # Count numbers that satisfy the constraint
        count = 0
        for val in max_values:
            if C == '>':
                if val > K:
                    count += 1
            elif C == '<':
                if val < K:
                    count += 1
            elif C == '=':
                if val == K:
                    count += 1
        
        # Game is a Nim game with count piles of size 1
        # The player who cannot make a move loses
        # If count is 0, first player loses
        # Else, if count is odd, first player wins (if X is 'D'), else second player wins
        if count == 0:
            results.append('C' if X == 'D' else 'D')
        else:
            if (count % 2 == 1) and (X == 'D'):
                results.append('D')
            else:
                results.append('C')
    
    print(''.join(results))

if __name__ == '__main__':
    solve()