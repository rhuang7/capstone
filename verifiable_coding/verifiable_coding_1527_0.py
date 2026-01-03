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
        
        # Check if B is not possible to obtain from A
        # For each position, if B[i] is 1, then A[i] must be 1
        # Because AND and XOR operations cannot set a bit to 1 if it was 0
        # OR operation can set a bit to 1, but only if at least one of the bits is 1
        # So, for B to be possible, all positions where B[i] is 1 must have A[i] as 1
        possible = True
        for i in range(len(A)):
            if B[i] == '1' and A[i] == '0':
                possible = False
                break
        
        if not possible:
            print("Unlucky Chef")
            continue
        
        # Now, we need to count the number of operations
        # We can use XOR operations to flip bits
        # AND operations can be used to set bits to 0
        # OR operations can be used to set bits to 1
        
        # Count the number of bits that need to be flipped
        # For each position, if B[i] != A[i], we need to flip it
        # But we can only flip bits using XOR operations
        # So, we need to count the number of differing bits
        diff = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                diff += 1
        
        # If there are no differing bits, it's already equal (handled earlier)
        # So, we need to flip all differing bits using XOR operations
        # Each XOR operation can flip two bits
        # So, the number of operations is (diff + 1) // 2
        
        # But we also need to consider that we can use AND and OR operations
        # However, the minimum number of operations is achieved by using XOR operations
        # So, the answer is (diff + 1) // 2
        
        print("Lucky Chef")
        print((diff + 1) // 2)

if __name__ == '__main__':
    solve()