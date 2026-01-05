import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        S = data[index]
        R = data[index + 1]
        index += 2
        
        N = len(S)
        if S == R:
            print(0)
            continue
        
        # Find the regions where S and R differ
        diff = []
        for i in range(N):
            if S[i] != R[i]:
                diff.append(i)
        
        # If there are no differences, output 0
        if not diff:
            print(0)
            continue
        
        # Calculate the minimum cost
        # The optimal way is to perform one operation per contiguous block of differences
        # So the number of operations is the number of contiguous blocks
        # The total length of all operations is the sum of the lengths of these blocks
        # The cost is (number of operations) * (total length of all operations)
        
        # Count the number of contiguous blocks
        block_count = 1
        for i in range(1, len(diff)):
            if diff[i] != diff[i - 1] + 1:
                block_count += 1
        
        # Total length of all operations is the total number of differing characters
        total_length = len(diff)
        
        print(block_count * total_length)
        
if __name__ == '__main__':
    solve()