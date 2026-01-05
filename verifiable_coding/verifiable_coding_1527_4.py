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
        
        # Check if B is not possible to achieve
        # For each position, if B[i] is 1, then A[i] must be 1
        # Otherwise, it's impossible
        possible = True
        for i in range(len(A)):
            if B[i] == '1' and A[i] == '0':
                possible = False
                break
        
        if not possible:
            print("Unlucky Chef")
            continue
        
        # Now check if B can be achieved with the operations
        # For each position, if B[i] is 1, then A[i] must be 1
        # Also, the number of 1s in B must be >= the number of 1s in A
        # Because operations can't increase the number of 1s
        count_A = A.count('1')
        count_B = B.count('1')
        if count_B < count_A:
            print("Unlucky Chef")
            continue
        
        # Now check if the number of 1s in B is equal to the number of 1s in A
        # If not, then it's impossible to achieve B from A
        if count_B != count_A:
            print("Unlucky Chef")
            continue
        
        # If all conditions are met, then it's possible
        # The minimum number of operations is the number of positions where A and B differ
        diff = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                diff += 1
        
        print("Lucky Chef")
        print(diff)