import sys
import bisect

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
    games = []
    for _ in range(M):
        C = data[idx]
        K = int(data[idx+1])
        X = data[idx+2]
        games.append((C, K, X))
        idx += 3

    # Preprocess the array to get all subarray maxima
    # Using a monotonic stack to find max in all subarrays
    # This is O(N) time
    max_subarrays = []
    stack = []
    for num in A:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
        max_subarrays.append(stack[-1])

    # For each game, process the constraints
    result = []
    for C, K, X in games:
        # Count the numbers that satisfy the constraint
        count = 0
        for val in max_subarrays:
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
        # The player who can't make a move loses
        # If count is 0, first player can't move, so second player wins
        # Otherwise, if count is non-zero, the game is determined by whether count is even or odd
        # If count is even, second player wins, else first player wins
        if count == 0:
            result.append('C' if X == 'D' else 'D')
        else:
            if (count % 2 == 1 and X == 'D') or (count % 2 == 0 and X == 'C'):
                result.append('D')
            else:
                result.append('C')
    print(''.join(result))