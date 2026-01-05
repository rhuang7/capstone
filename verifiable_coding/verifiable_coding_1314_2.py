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
        
        # Generate all non-empty continuous subarrays and find their maximum
        max_list = []
        for i in range(N):
            current_max = A[i]
            max_list.append(current_max)
            for j in range(i + 1, N):
                current_max = max(current_max, A[j])
                max_list.append(current_max)
        
        # Count numbers satisfying the constraint
        count = 0
        for num in max_list:
            if C == '>':
                if num > K:
                    count += 1
            elif C == '<':
                if num < K:
                    count += 1
            elif C == '=':
                if num == K:
                    count += 1
        
        # Game is a variant of Nim game
        # The player who cannot make a move loses
        # So if count is 0, first player loses
        # Else, if count is odd, first player wins, else second player wins
        if count == 0:
            results.append('C' if X == 'D' else 'D')
        else:
            if count % 2 == 1:
                results.append('D' if X == 'D' else 'C')
            else:
                results.append('C' if X == 'D' else 'D')
    
    print(''.join(results))

if __name__ == '__main__':
    solve()