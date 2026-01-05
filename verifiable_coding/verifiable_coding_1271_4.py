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
        Q = int(data[idx])
        idx += 1
        queries = []
        for _ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        
        S = set()
        for X in queries:
            new_elements = set()
            for y in S:
                new_elements.add(y ^ X)
            for y in new_elements:
                if y not in S:
                    S.add(y)
            S.add(X)
            even = 0
            odd = 0
            for num in S:
                cnt = bin(num).count('1')
                if cnt % 2 == 0:
                    even += 1
                else:
                    odd += 1
            results.append(f"{even} {odd}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()