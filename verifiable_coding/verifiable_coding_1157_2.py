import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        hearts = list(map(int, data[idx:idx+K]))
        idx += K
        
        # Convert to 0-based index
        hearts = [x-1 for x in hearts]
        
        # Precompute all possible rectangles
        # For large N and M, it's not feasible to generate all rectangles
        # So we use inclusion-exclusion and coordinate compression
        
        # Sort the hearts
        hearts.sort()
        
        # Coordinate compression
        coords = set(hearts)
        coord_list = sorted(coords)
        coord_map = {x: i for i, x in enumerate(coord_list)}
        size = len(coord_list)
        
        # Precompute prefix sums
        prefix = [0] * (size + 1)
        for i in range(size):
            prefix[i+1] = prefix[i] + 1
        
        # Count number of rectangles that include each heart
        # For each heart, count how many rectangles include it
        # This is equivalent to the number of rectangles that include the heart's position
        
        # For a heart at (i, j), the number of rectangles that include it is:
        # (i+1) * (j+1) * (N - i) * (M - j)
        # But since we have multiple hearts, we need to find the number of rectangles that include at least one heart
        
        # Instead, we can use inclusion-exclusion: total number of rectangles - number of rectangles that include none of the hearts
        
        # Total number of rectangles in an N x M grid
        total_rectangles = N * M * (N * M + 1) // 2
        
        # Compute number of rectangles that include none of the hearts
        # For this, we need to find the number of rectangles that lie entirely in the grid excluding the hearts
        
        # We can use the inclusion-exclusion principle here, but for large N and M, it's not feasible to do it directly
        
        # So we use coordinate compression and inclusion-exclusion on the compressed coordinates
        
        # We sort the hearts and use the inclusion-exclusion principle on the compressed coordinates
        
        # For each heart, we compute the number of rectangles that include it
        # Then use inclusion-exclusion to compute the total number of rectangles that include at least one heart
        
        # But this is not feasible for K up to 1e5
        
        # So we use a different approach: for each heart, we compute the number of rectangles that include it, then subtract the overlaps
        
        # However, this is also not feasible for K up to 1e5
        
        # So we use a different approach: for each heart, we compute the number of rectangles that include it, then use the inclusion-exclusion principle on the compressed coordinates
        
        # But again, this is not feasible for K up to 1e5
        
        # So we use the following approach:
        # For each heart, compute the number of rectangles that include it
        # Then sum all these numbers, and divide by the total number of rectangles
        
        # But this will overcount rectangles that include multiple hearts
        
        # So we need to use the inclusion-exclusion principle
        
        # However, for large K, this is not feasible
        
        # So we use the following approach:
        # For each heart, compute the number of rectangles that include it
        # Then use the inclusion-exclusion principle on the compressed coordinates
        
        # But again, for large K, this is not feasible
        
        # So we use the following approach:
        # For each heart, compute the number of rectangles that include it
        # Then sum all these numbers, and divide by the total number of rectangles
        
        # This is the expected value of the number of hearts in a random rectangle
        
        # So the expected value is (sum over all hearts of the number of rectangles that include it) / total number of rectangles
        
        # So we compute this sum
        
        total = 0
        for x in hearts:
            i = x // M
            j = x % M
            # Number of rectangles that include this cell
            # The number of rectangles that include this cell is:
            # (i+1) * (j+1) * (N - i) * (M - j)
            total += (i+1) * (j+1) * (N - i) * (M - j)
        
        expected = total / total_rectangles
        results.append(expected)
    
    for res in results:
        print(f"{res:.12f}")

if __name__ == '__main__':
    solve()