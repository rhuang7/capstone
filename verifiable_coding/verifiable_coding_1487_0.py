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
        X = int(data[idx])
        idx += 1
        
        a_boxes = 0
        b_boxes = 0
        a_candies = 0
        b_candies = 0
        left = 0
        right = N - 1
        
        while left <= right:
            if a_candies * X < b_candies:
                a_boxes += 1
                a_candies += C[left]
                left += 1
            elif b_candies < a_candies * X:
                b_boxes += 1
                b_candies += C[right]
                right -= 1
            else:
                if a_boxes > b_boxes:
                    a_boxes += 1
                    a_candies += C[left]
                    left += 1
                else:
                    b_boxes += 1
                    b_candies += C[right]
                    right -= 1
        results.append(f"{a_boxes} {b_boxes}")
    
    print('\n'.join(results))