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
        
        # Find the regions where S and R differ
        diff = [i for i in range(N) if S[i] != R[i]]
        if not diff:
            print(0)
            continue
        
        # Calculate the minimum cost
        # The optimal strategy is to perform one operation per contiguous block of differing characters
        # So the number of operations is the number of contiguous blocks
        # The total length of all operations is the sum of the lengths of these blocks
        # The cost is (number of operations) * (total length of all operations)
        # But since each operation is a contiguous block, the total length is N
        # So the cost is (number of operations) * N
        # So we need to find the number of contiguous blocks of differing characters
        
        # Count the number of contiguous blocks
        blocks = 1
        for i in range(1, len(diff)):
            if diff[i] != diff[i-1] + 1:
                blocks += 1
        
        print(blocks * N)
        
if __name__ == '__main__':
    solve()