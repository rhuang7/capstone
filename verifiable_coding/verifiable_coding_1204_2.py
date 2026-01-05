import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        S = data[index]
        R = data[index+1]
        index += 2
        
        N = len(S)
        if S == R:
            print(0)
            continue
        
        # Find the positions where S and R differ
        diff = []
        for i in range(N):
            if S[i] != R[i]:
                diff.append(i)
        
        # If no differences, output 0
        if not diff:
            print(0)
            continue
        
        # Calculate the minimum cost
        # The optimal strategy is to perform operations on contiguous segments of differences
        # So we can group the differences into contiguous segments and calculate the cost
        # For each segment, the cost is (number of operations) * (length of segment)
        # Since we can perform one operation per segment, the cost is length of segment
        # So the total cost is the sum of the lengths of the contiguous segments of differences
        
        # Group the differences into contiguous segments
        segments = []
        start = diff[0]
        for i in range(1, len(diff)):
            if diff[i] == diff[i-1] + 1:
                continue
            else:
                segments.append((start, diff[i-1]))
                start = diff[i]
        segments.append((start, diff[-1]))
        
        total_cost = 0
        for seg in segments:
            total_cost += (seg[1] - seg[0] + 1)
        
        print(total_cost)

if __name__ == '__main__':
    solve()