import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for case in range(1, T + 1):
        L = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if K == 0:
            results.append(f"Case {case}: 0")
            continue
        
        if K > L:
            results.append(f"Case {case}: 0")
            continue
        
        # Number of valid triangles of side length K
        # Valid triangles must have their base at a distance less than the height of the triangle
        # The height of a triangle of side K is K * (sqrt(3)/2), but we only need to count based on layers
        # For a triangle of side K, it can be placed in layers from 1 to (L - K)
        # Each layer contributes (L - K - i + 1) * (L - K - i + 1) triangles
        # But we need to consider the orientation and direction
        # For each valid triangle, there are 3 orientations: pointing up, down, left, right
        # But in this problem, only triangles with base parallel to BC are considered
        # So for each layer, the number of triangles is (L - K - i + 1) * (L - K - i + 1)
        # But we need to sum over all valid layers
        total = 0
        for i in range(1, L - K + 1):
            count = (L - K - i + 1) * (L - K - i + 1)
            total += count
        
        results.append(f"Case {case}: {total}")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()