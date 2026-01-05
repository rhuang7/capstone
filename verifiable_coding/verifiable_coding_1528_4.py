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
        coins = data[idx:idx+N]
        idx += N
        # Simulate the operations
        # We'll track the number of flips and the current state of the coins
        # We'll process from the end to the beginning
        # Since each flip affects all coins to the left of the removed one
        # We can track the number of flips and apply them at the end
        # We'll also track the number of coins remaining
        # We'll process the coins from right to left
        # We'll keep track of the number of flips
        flips = 0
        heads = 0
        # We'll process from the end to the beginning
        for i in range(N-1, -1, -1):
            # If we have performed K operations, we stop
            if K == 0:
                break
            # If the current coin is to be removed
            if K > 0:
                # Check if the coin was heads before removal
                if coins[i] == 'H':
                    flips += 1
                # Decrement K as we removed one coin
                K -= 1
            # Apply the flips to the current coin
            if flips % 2 == 1:
                if coins[i] == 'H':
                    heads += 1
                else:
                    heads -= 1
        results.append(str(heads))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()