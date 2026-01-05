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
        idx += 1
        K = int(data[idx])
        idx += 1
        X = data[idx]
        idx += 1
        games.append((C, K, X))
    
    # Preprocess the array to get all subarray maxima
    # Using a monotonic stack approach to find all subarray maxima
    # This is O(N) time
    maxima = []
    stack = []
    for num in A:
        while stack and stack[-1][0] <= num:
            stack.pop()
        stack.append((num, len(maxima)))
        maxima.append(num)
    # Now, maxima contains all subarray maxima in order
    # We need to count the number of elements in the maxima array that satisfy the constraint for each game
    
    res = []
    for C, K, X in games:
        # Count the number of elements in maxima that satisfy the constraint
        count = 0
        if C == '>':
            count = len(maxima) - bisect.bisect_right(maxima, K)
        elif C == '<':
            count = bisect.bisect_left(maxima, K)
        elif C == '=':
            count = bisect.bisect_right(maxima, K) - bisect.bisect_left(maxima, K)
        # Now, determine the winner based on the count and who starts
        if count == 0:
            res.append('C' if X == 'D' else 'D')
        else:
            # Game is equivalent to a Nim game with count piles of size 1
            # The winner is determined by whether count is a winning position
            # In Nim, if the number of piles is non-zero and the first player can make a move, they win
            # Since all piles are size 1, the first player wins if count is non-zero and it's their turn
            # If count is even, the second player wins; if odd, the first player wins
            if count % 2 == 1:
                res.append('D' if X == 'D' else 'C')
            else:
                res.append('C' if X == 'D' else 'D')
    
    print(''.join(res))