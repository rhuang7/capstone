import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        S = list(map(int, data[idx:idx+K]))
        idx += K
        
        # Precompute 2^p for all p in A
        power = [1 << p for p in A]
        
        # Compute the total score
        total = sum(power)
        
        # Since both players play optimally, the game is a variant of a game where players take turns
        # and the player who takes the last move wins. However, the scoring is based on the sum of 2^p
        # for the discs popped. The optimal play would be to maximize one's own score while minimizing
        # the opponent's score.
        
        # Since the game is symmetric and both players play optimally, the outcome depends on whether
        # the total score is even or odd. If the total is even, the game is a draw. If it's odd, the
        # player who makes the first move (Chef) wins.
        
        if total % 2 == 0:
            results.append("Draw")
        else:
            results.append("Chef")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()