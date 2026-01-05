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
        queries = list(map(int, data[idx:idx+Q]))
        idx += Q
        
        S = set()
        even = 0
        odd = 0
        
        for X in queries:
            new_elements = set()
            for y in S:
                new_elements.add(y ^ X)
            new_elements.add(X)
            for elem in new_elements:
                if elem in S:
                    continue
                S.add(elem)
                count = bin(elem).count('1')
                if count % 2 == 0:
                    even += 1
                else:
                    odd += 1
            results.append(f"{even} {odd}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()