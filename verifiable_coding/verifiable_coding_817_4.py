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
        
        # The minimum cost is the sum of all elements in the array
        # Because each operation replaces two elements with their XOR, which is equivalent to removing the sum of the two elements
        # So the minimum cost is the sum of all elements
        results.append(sum(A))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()