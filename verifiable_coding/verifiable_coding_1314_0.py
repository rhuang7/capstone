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
        # To optimize, precompute all max values of subarrays
        max_subarrays = []
        for i in range(N):
            current_max = A[i]
            max_subarrays.append(current_max)
            for j in range(i + 1, N):
                current_max = max(current_max, A[j])
                max_subarrays.append(current_max)
        
        # Count numbers based on constraint
        count = 0
        for num in max_subarrays:
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
        # Otherwise, it's a standard Nim game with count piles of size 1
        # The winner is determined by whether count is 0 or not and who starts
        if count == 0:
            results.append('C' if X == 'D' else 'D')
        else:
            # In standard Nim game with count piles of size 1, the winner is determined by whether count is 0 or not
            # If count is non-zero, the first player wins if count is non-zero and count is not zero
            # But since all piles are size 1, the game is just a simple count
            # If count is even, second player wins; if odd, first player wins
            if X == 'D':
                if count % 2 == 1:
                    results.append('D')
                else:
                    results.append('C')
            else:
                if count % 2 == 1:
                    results.append('C')
                else:
                    results.append('D')
    
    print(''.join(results))

if __name__ == '__main__':
    solve()