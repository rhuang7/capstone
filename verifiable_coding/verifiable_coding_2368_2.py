import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Find the minimum possible value for a_i and b_i
        # The final a_i and b_i must be such that a_i <= original a_i and b_i <= original b_i
        # So the minimum possible a_i is the minimum of a, and the minimum possible b_i is the minimum of b
        min_a = min(a)
        min_b = min(b)
        
        # Calculate the total moves needed
        total_moves = 0
        
        # For each gift, calculate the moves needed to reduce a_i to min_a and b_i to min_b
        for i in range(n):
            total_moves += (a[i] - min_a)
            total_moves += (b[i] - min_b)
        
        results.append(total_moves)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()