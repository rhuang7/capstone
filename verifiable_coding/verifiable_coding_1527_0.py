import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        A = data[idx]
        idx += 1
        B = data[idx]
        idx += 1
        
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
            if a[i] > b[i]:
                possible = False
                break
        
        if not possible:
            results.append("Unlucky Chef")
            continue
        
        # Count the number of positions where A and B differ
        diff = 0
        for i in range(n):
            if a[i] != b[i]:
                diff += 1
        
        # If there are no differences, it's already equal (handled earlier)
        if diff == 0:
            results.append("Lucky Chef")
            results.append("0")
            continue
        
        # For each differing position, we need at least one operation
        # But some operations can fix multiple differences
        # We need to count the minimum number of operations
        # For each bit that is 1 in A but 0 in B, we need to flip it
        # We can flip multiple bits with one XOR operation
        # So the minimum number of operations is the number of differing bits
        results.append("Lucky Chef")
        results.append(str(diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()