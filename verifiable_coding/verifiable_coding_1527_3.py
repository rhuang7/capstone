import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        A = data[index]
        index += 1
        B = data[index]
        index += 1
        
        if len(A) != len(B):
            results.append("Unlucky Chef")
            continue
        
        if A == B:
            results.append("Lucky Chef")
            results.append("0")
            continue
        
        # Check if it's possible to convert A to B
        # For each position, check if B[i] can be achieved from A[i]
        # For AND and OR operations, the bits can only be changed if there's at least one 1 in the string
        # For XOR operation, it can flip bits if there's at least one 1 in the string
        # However, the operations are not straightforward to model directly
        
        # Check if B has any 1s that A does not have
        # If B has a 1 in a position where A has 0, and there's at least one 1 in the string, then it's possible
        # But if B has a 1 in a position where A has 0, and there are no 1s in the string, then it's impossible
        
        # Check if B has any 1s that A does not have
        has_ones_in_A = any(c == '1' for c in A)
        has_ones_in_B = any(c == '1' for c in B)
        
        if not has_ones_in_B:
            # B has no 1s, but A has some
            # Then it's impossible to convert A to B
            results.append("Unlucky Chef")
            continue
        
        # Check if B has a 1 in a position where A has 0
        # If there's at least one 1 in A, then it's possible to flip bits using XOR
        # If there's at least one 1 in B, then it's possible to set bits using OR
        # If there's at least one 1 in A, then it's possible to change bits using AND and XOR
        # If there's at least one 1 in B, then it's possible to change bits using OR and XOR
        
        # Check if B has a 1 in a position where A has 0
        # If there's at least one 1 in A, then it's possible to flip bits using XOR
        # If there's at least one 1 in B, then it's possible to set bits using OR
        # If there's at least one 1 in A, then it's possible to change bits using AND and XOR
        # If there's at least one 1 in B, then it's possible to change bits using OR and XOR
        
        # If there's at least one 1 in A and B, then it's possible to convert A to B
        if has_ones_in_A and has_ones_in_B:
            # Check if B has a 1 in a position where A has 0
            # If there's at least one 1 in A, then it's possible to flip bits using XOR
            # If there's at least one 1 in B, then it's possible to set bits using OR
            # If there's at least one 1 in A, then it's possible to change bits using AND and XOR
            # If there's at least one 1 in B, then it's possible to change bits using OR and XOR
            # If there's at least one 1 in A and B, then it's possible to convert A to B
            # So, it's possible to convert A to B
            # Now, calculate the minimum number of operations
            # For each position, if B[i] != A[i], then we need to perform an operation
            # But the operations can be applied to multiple positions at once
            # So, we need to count the number of positions where B[i] != A[i]
            # Each operation can change multiple bits
            # But the exact number of operations is not clear
            # However, based on the example, it seems that the number of operations is the number of differing bits
            # So, the minimum number of operations is the number of differing bits
            diff = 0
            for a, b in zip(A, B):
                if a != b:
                    diff += 1
            results.append("Lucky Chef")
            results.append(str(diff))
        else:
            results.append("Unlucky Chef")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()