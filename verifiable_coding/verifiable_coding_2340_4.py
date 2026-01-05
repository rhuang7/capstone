import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        
        # We need to check if the permutation can be split into two arrays a and b
        # such that p is the merge of a and b as per the given rules
        # We can simulate the merge process in reverse
        
        # Initialize two pointers for a and b
        a_ptr = 0
        b_ptr = 0
        
        # We'll build the arrays a and b in reverse order
        a = []
        b = []
        
        for num in p:
            if a_ptr < n and (b_ptr >= n or num < p[b_ptr]):
                # This element belongs to a
                a.append(num)
                a_ptr += 1
            else:
                # This element belongs to b
                b.append(num)
                b_ptr += 1
        
        # Check if a and b have exactly n elements each
        if len(a) != n or len(b) != n:
            results.append("NO")
            continue
        
        # Check if a and b have no common elements
        if set(a) & set(b):
            results.append("NO")
            continue
        
        # Check if the merge of a and b equals p
        # We need to simulate the merge process
        def merge(a, b):
            res = []
            while a and b:
                if a[0] < b[0]:
                    res.append(a[0])
                    a = a[1:]
                else:
                    res.append(b[0])
                    b = b[1:]
            res.extend(a)
            res.extend(b)
            return res
        
        if merge(a, b) == p:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()