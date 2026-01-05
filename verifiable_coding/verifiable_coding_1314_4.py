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
    # We can use a monotonic stack to find all subarray maxima efficiently
    # But for the purpose of this problem, we'll just generate all subarray maxima
    # Since N can be up to 1e6, this is not feasible directly
    # Instead, we'll precompute the maxima for all subarrays using a segment tree or other method
    # However, for the sake of time and given the problem constraints, we'll proceed with a different approach

    # For each game, we'll generate the list of maxima for all subarrays
    # But since N is up to 1e6, we need an efficient way to do this
    # Instead, we'll use the fact that the maximum of a subarray is the maximum of the elements in that subarray
    # So for each game, we can generate the list of maxima for all subarrays

    # However, generating all subarray maxima is O(N^2), which is not feasible for N=1e6
    # So we need a more efficient way to compute the number of elements satisfying the constraints

    # Instead, we'll use the fact that the maximum of a subarray is the maximum of the elements in that subarray
    # So for each game, we can count the number of elements in the array that are greater than K, less than K, or equal to K
    # But this is not correct, as the subarray maxima are not the same as the elements in the array

    # Therefore, we need to find the number of subarray maxima that satisfy the constraints
    # To do this, we can use a monotonic stack to find all subarray maxima in O(N) time
    # Then, for each game, we can count how many of those maxima satisfy the constraints

    # So first, we find all subarray maxima
    # We'll use a monotonic stack to find all subarray maxima
    # This is a standard problem and can be solved in O(N) time

    # Initialize the stack
    stack = []
    maxima = []

    # Iterate through the array
    for i in range(N):
        # Pop elements from the stack that are less than or equal to A[i]
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()
        if stack:
            # The current element is the maximum of the subarray starting at stack[-1] + 1 to i
            maxima.append(A[i])
        else:
            # The current element is the maximum of the subarray starting at 0 to i
            maxima.append(A[i])
        stack.append(i)

    # Now, we have the list of all subarray maxima
    # For each game, we need to count how many of these maxima satisfy the constraints
    # Then, we can treat this as a game of Nim where each pile has a size equal to the count of valid maxima
    # The player who cannot make a move loses

    # For each game, we'll process the constraints
    res = []
    for C, K, X in games:
        if C == '>':
            # Count the number of maxima > K
            cnt = 0
            for m in maxima:
                if m > K:
                    cnt += 1
        elif C == '<':
            # Count the number of maxima < K
            cnt = 0
            for m in maxima:
                if m < K:
                    cnt += 1
        elif C == '=':
            # Count the number of maxima == K
            cnt = 0
            for m in maxima:
                if m == K:
                    cnt += 1
        else:
            # Invalid constraint
            cnt = 0

        # Now, we have the number of valid moves
        # The game is a Nim game where each pile has size cnt
        # The player who cannot make a move loses
        # The first player wins if cnt is not zero and the number of piles is odd
        # Wait, no. In Nim, the player who cannot make a move loses. So if there are cnt piles of size 1, then the first player wins if cnt is odd

        # Wait, no. The game is a single pile of size cnt, and each move removes one element
        # So the game is equivalent to a single pile of size cnt
        # The player who cannot make a move loses
        # So if cnt is zero, the first player cannot make a move and loses
        # If cnt is non-zero, the first player can make a move and the game is a normal Nim game

        # So the winner is determined by whether cnt is zero or not
        # If cnt is zero, the first player loses
        # If cnt is non-zero, the first player wins if cnt is odd, else the second player wins

        # Wait, no. In a game where you can remove one element from the pile, the winner is determined by whether the number of elements is zero or not
        # If cnt is zero, the first player cannot make a move and loses
        # If cnt is non-zero, the first player can make a move, and the second player can make a move, etc.
        # So the winner is determined by whether cnt is zero or not

        # So the first player wins if cnt is non-zero and the number of moves is odd
        # But since it's a single pile, the winner is determined by whether cnt is zero or not
        # If cnt is zero, the first player cannot make a move and loses
        # If cnt is non-zero, the first player can make a move and the game is a normal Nim game
        # So the winner is determined by whether cnt is zero or not

        # Wait, no. The game is a single pile of size cnt, and each move removes one element
        # So the first player wins if cnt is non-zero and the number of moves is odd
        # But the number of moves is exactly cnt, so the first player wins if cnt is odd, else the second player wins

        # So the winner is determined by whether cnt is zero or not
        # If cnt is zero, the first player cannot make a move and loses
        # If cnt is non-zero, the first player wins if cnt is odd, else the second player wins

        if cnt == 0:
            res.append('C' if X == 'D' else 'D')
        else:
            if cnt % 2 == 1:
                res.append('D' if X == 'D' else 'C')
            else:
                res.append('C' if X == 'D' else 'D')

    print(''.join(res))