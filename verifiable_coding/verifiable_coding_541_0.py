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
        N = int(data[idx])
        idx += 1
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_height = 0
        color_count = {}
        
        for i in range(N):
            color = C[i]
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
            
            # Check if we can form a tower ending at i
            # We need to have at least one triangle left (the roof)
            # So the number of triangles must be (2k + 1), where k is the height
            # So the total number of triangles in the segment must be odd
            # And the number of triangles of each color must be even (except one)
            # So for each color, the count must be even, except one color which has an odd count
            # So the total number of triangles must be odd, and the sum of all color counts must be odd
            # Also, the number of triangles of each color must be even, except one which is odd
            # So for each color, the count must be even, except one which is odd
            # So the total number of triangles must be odd, and the sum of all color counts must be odd
            # And the number of colors with odd count must be exactly 1
            
            # Check if the current segment can form a tower
            # We need to have exactly one color with an odd count, and the rest even
            odd_count = 0
            for c in color_count.values():
                if c % 2 != 0:
                    odd_count += 1
            if odd_count == 1:
                # The total number of triangles in the segment is odd
                # So the height is (total_triangles - 1) // 2
                total_triangles = i + 1
                height = (total_triangles - 1) // 2
                if height > max_height:
                    max_height = height
        
        results.append(str(max_height))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()