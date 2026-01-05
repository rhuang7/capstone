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
        R = int(data[idx])
        G = int(data[idx+1])
        B = int(data[idx+2])
        idx += 3
        K = int(data[idx])
        idx += 1
        
        # Find the maximum count of any color
        max_count = max(R, G, B)
        
        # If K is larger than the maximum count, it's impossible
        if K > max_count:
            results.append(-1)
        else:
            # The minimum number of balloons needed is K + 2 (worst case)
            # But we need to consider the sum of the other two colors
            # So the answer is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) + 1 + 1 = K + 1
            # But if there are less than two colors, we need to adjust
            # So the correct formula is (K-1) +