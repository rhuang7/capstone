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
        
        if A == B:
            results.append("Lucky Chef")
            results.append("0")
            continue
        
        n = len(A)
        a = [int(c) for c in A]
        b = [int(c) for c in B]
        
        # Check if it's possible to convert A to B
        possible = True
        for i in range(n):
            if a[i] != b[i]:
                possible = False
                break
        
        if not possible:
            results.append("Unlucky Chef")
            continue
        
        # Check if B has more 1s than A
        if sum(b) > sum(a):
            results.append("Unlucky Chef")
            continue
        
        # Check if B has less 1s than A
        if sum(b) < sum(a):
            # Check if B can be achieved by some operations
            # If B has less 1s than A, it's possible only if B is a subset of A
            # But since we can only decrease the number of 1s via AND and XOR operations
            # We need to check if B is a subset of A
            # For each bit in B, it must be 0 or 1 in A
            for i in range(n):
                if b[i] == 1 and a[i] == 0:
                    possible = False
                    break
            if not possible:
                results.append("Unlucky Chef")
                continue
        
        # If all checks pass, it's possible
        # Now calculate the minimum number of operations
        # We need to find the number of positions where A and B differ
        diff = 0
        for i in range(n):
            if a[i] != b[i]:
                diff += 1
        
        # For each differing bit, we need at least one operation
        # But some operations can fix multiple bits
        # However, in the worst case, each differing bit requires at least one operation
        # So the minimum number of operations is the number of differing bits
        results.append("Lucky Chef")
        results.append(str(diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()