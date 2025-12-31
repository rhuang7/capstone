import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        Q = int(data[index])
        index += 1
        queries = []
        for _ in range(Q):
            queries.append(int(data[index]))
            index += 1
        
        S = set()
        E = 0
        O = 0
        
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
                    E += 1
                else:
                    O += 1
            results.append(f"{E} {O}")
        
    print("\n".join(results))

if __name__ == '__main__':
    solve()