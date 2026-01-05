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
    games = []
    for _ in range(M):
        C = data[idx]
        idx += 1
        K = int(data[idx])
        idx += 1
        X = data[idx]
        idx += 1
        games.append((C, K, X))
    
    # Preprocess the array to get all subarray maxima
    # Using a monotonic stack to find all subarray maxima in O(N) time
    # This is a standard problem and can be solved with a monotonic stack
    # We'll store all subarray maxima in a list
    maxima = []
    stack = []
    for num in A:
        while stack and stack[-1] < num:
            stack.pop()
        if stack:
            maxima.append(stack[-1])
        else:
            maxima.append(num)
        stack.append(num)
    
    # Now, for each game, count the numbers that satisfy the constraint
    # and determine the winner based on the game theory rules
    result = []
    for C, K, X in games:
        count = 0
        for num in maxima:
            if C == '>':
                if num > K:
                    count += 1
            elif C == '<':
                if num < K:
                    count += 1
            elif C == '=':
                if num == K:
                    count += 1
        # Game is a variant of Nim game where each move removes one object
        # The player who cannot make a move loses
        # So if count is zero, the first player cannot move and loses
        # If count is non-zero, the winner depends on whether count is even or odd
        # If count is zero, the first player loses
        # If count is non-zero, the first player wins if count is odd, else loses
        if count == 0:
            result.append('C' if X == 'D' else 'D')
        else:
            if count % 2 == 1:
                result.append('D' if X == 'D' else 'C')
            else:
                result.append('C' if X == 'D' else 'D')
    
    print(''.join(result))