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
        diff = []
        for i in range(N):
            if S[i] != R[i]:
                diff.append(i)
        
        # If no differences, output 0
        if not diff:
            print(0)
            continue
        
        # Calculate the minimum cost
        # The optimal way is to perform operations on contiguous blocks of differing positions
        # So we group the differing positions into contiguous blocks
        # For each block, the cost is (number of operations) * (length of block)
        # Since we can perform one operation per block, the cost is length of block
        # So total cost is sum of lengths of contiguous differing blocks
        cost = 0
        prev = diff[0]
        for i in range(1, len(diff)):
            if diff[i] != diff[i-1] + 1:
                cost += diff[i] - prev
                prev = diff[i]
        cost += len(diff) - prev
        
        print(cost)

if __name__ == '__main__':
    solve()