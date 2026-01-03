import sys

def count_ones(x):
    return bin(x).count('1')

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        Q = int(data[index])
        index += 1
        queries = list(map(int, data[index:index+Q]))
        index += Q
        
        S = set()
        E = 0
        O = 0
        
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
            for x in S:
                if count_ones(x) % 2 == 0:
                    even += 1
                else:
                    odd += 1
            print(even, odd)

if __name__ == '__main__':
    solve()