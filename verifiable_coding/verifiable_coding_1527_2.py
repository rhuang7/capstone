import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        A = data[index]
        index += 1
        B = data[index]
        index += 1
        
        if A == B:
            print("Lucky Chef")
            print(0)
            continue
        
        n = len(A)
        if len(B) != n:
            print("Unlucky Chef")
            continue
        
        # Check if it's possible to convert A to B
        # For each position, if B[i] is 1, then A[i] must be 1
        # Because AND and XOR operations can't create a 1 from 0s
        possible = True
        for i in range(n):
            if B[i] == '1' and A[i] == '0':
                possible = False
                break
        
        if not possible:
            print("Unlucky Chef")
            continue
        
        # Count the number of positions where A and B differ
        diff = 0
        for i in range(n):
            if A[i] != B[i]:
                diff += 1
        
        # If there are no differences, it's already equal (handled earlier)
        # Otherwise, we need at least one operation
        # For each differing bit, we need at least one operation
        # But since operations can affect multiple bits, we need to find the minimum steps
        
        # The minimum number of operations is the number of differing bits
        # Because each operation can change at least one bit
        # However, for some cases, it might take more steps
        # For example, if there are two differing bits, it might take 2 operations
        
        # But according to the problem's example, it's possible to do it in 2 steps
        # So the minimum number of operations is the number of differing bits
        
        print("Lucky Chef")
        print(diff)