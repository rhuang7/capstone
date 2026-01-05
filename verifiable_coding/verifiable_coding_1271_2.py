import sys

def count_bits(x):
    return bin(x).count('1')

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
        E = 0
        O = 0
        
        for X in queries:
            new_elements = set()
            for y in S:
                new_elements.add(y ^ X)
            new_elements.add(X)
            to_add = new_elements - S
            for val in to_add:
                S.add(val)
                cnt = count_bits(val)
                if cnt % 2 == 0:
                    E += 1
                else:
                    O += 1
            results.append(f"{E} {O}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()