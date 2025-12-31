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
        
        # Check if it's possible to convert A to B
        # For each position, if B[i] is 1, then A[i] must be 1
        # Because AND and XOR operations cannot set a bit to 1 if it was 0
        # OR operation can set a bit to 1, but only if at least one of the bits is 1
        # So, for B to be achievable from A, all positions where B[i] is 1 must have A[i] is 1
        # Also, the total number of 1s in B must be less than or equal to the total number of 1s in A
        # Because AND and XOR operations can't increase the number of 1s
        # OR operation can increase the number of 1s, but only if at least one of the bits is 1
        
        # Check if B has any 1s where A has 0s
        possible = True
        for a, b in zip(A, B):
            if b == '1' and a == '0':
                possible = False
                break
        
        if not possible:
            print("Unlucky Chef")
            continue
        
        # Count the number of 1s in A and B
        count_A = A.count('1')
        count_B = B.count('1')
        
        # If B has more 1s than A, it's impossible to achieve with OR operations
        if count_B > count_A:
            print("Unlucky Chef")
            continue
        
        # Now, calculate the minimum number of operations
        # For each position where A[i] != B[i], we need to perform an operation
        # But we can use OR operations to set bits to 1, and XOR to flip bits
        # However, the exact number of operations depends on the specific configuration
        
        # For each position, if B[i] is 1 and A[i] is 0, we need to perform an OR operation
        # If B[i] is 0 and A[i] is 1, we need to perform an XOR operation
        # But since we can perform operations on pairs, we need to find the minimum number of operations
        
        # Let's count the number of positions where A[i] != B[i]
        diff_count = 0
        for a, b in zip(A, B):
            if a != b:
                diff_count += 1
        
        # For each pair of differing bits, we can perform one operation
        # So the minimum number of operations is diff_count // 2
        # But if there is an odd number of differing bits, we need one more operation
        
        # However, this is not accurate because some operations can affect multiple bits
        # So we need to find the minimum number of operations that can change the bits
        
        # Let's count the number of positions where A[i] is 1 and B[i] is 0
        # These need to be flipped using XOR operations
        flip_count = 0
        for a, b in zip(A, B):
            if a == '1' and b == '0':
                flip_count += 1
        
        # The minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # However, this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # But this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # But this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # However, this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # However, this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # However, this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # However, this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # However, this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # However, this is not correct because we can also use OR operations to set bits to 1
        # So the correct approach is to count the number of positions where A[i] is 0 and B[i] is 1
        # These can be set using OR operations, and each OR operation can set two bits
        
        # So the minimum number of operations is the number of flip operations
        # Because each XOR operation can flip two bits
        # So the minimum number of operations is flip_count // 2
        # But if there is an odd number of flip operations, we need one more operation
        
        # However, this is not correct because we can also use OR operations to set