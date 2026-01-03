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
        N, X = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        total_sum = sum(A)
        remaining_piles = N - X
        
        # Calculate the sum of the remaining piles
        # Since all piles are removed in X moves, the remaining piles are N - X
        # But the sum depends on which piles are removed
        # To determine the winner, we need to find the sum of the remaining piles after X moves
        
        # The optimal play is to remove piles in a way that makes the sum of the remaining piles even or odd
        # We need to find the sum of the remaining piles after X moves
        
        # The sum of the remaining piles is total_sum - sum of the removed piles
        # We need to choose X piles to remove such that the sum of the remaining is odd or even
        
        # To determine the winner, we need to see if it's possible for the sum of the remaining piles to be odd or even
        # Based on the parity of the total_sum and the number of piles removed
        
        # If X is even, the parity of the sum of the remaining piles is the same as the total_sum
        # If X is odd, the parity of the sum of the remaining piles is the opposite of the total_sum
        
        if X % 2 == 0:
            if total_sum % 2 == 0:
                results.append("Jesse")
            else:
                results.append("Walter")
        else:
            if total_sum % 2 == 0:
                results.append("Walter")
            else:
                results.append("Jesse")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()