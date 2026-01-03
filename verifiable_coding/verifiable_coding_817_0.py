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
        # Because any operation reduces the array length but the sum remains the same
        # as the XOR of two numbers is equal to their sum in binary if they are distinct
        # but in general, the sum of the array remains the same as the sum of the elements
        # because XOR is not the same as addition, but the problem says the cost is the sum
        # of the elements in the array, so the minimum cost is the sum of the original array
        results.append(sum(A))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()