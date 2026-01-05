import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Group the sequence into runs of equal elements
        groups = []
        current_val = A[0]
        count = 1
        for i in range(1, N):
            if A[i] == current_val:
                count += 1
            else:
                groups.append(count)
                current_val = A[i]
                count = 1
        groups.append(count)
        
        # For each group, if its length is odd, we need to do something
        # We can either delete one element (cost 1) or insert one element (cost 1)
        # But we want to minimize the total operations
        
        # We can try all possible ways to make all group lengths even
        # The optimal way is to delete or insert elements to make all group lengths even
        # The minimal operations is the number of groups with odd lengths
        
        odd_count = 0
        for g in groups:
            if g % 2 != 0:
                odd_count += 1
        
        # The minimal operations is the number of odd groups
        results.append(odd_count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()