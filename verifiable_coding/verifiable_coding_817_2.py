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
        # Because any operation replaces two elements with their XOR, which is
        # equivalent to the sum of the two elements minus twice their AND (since XOR = A ^ B = (A + B) - 2*(A & B))
        # However, since we are minimizing the sum, the optimal strategy is to keep the elements as they are
        # because any operation reduces the number of elements but the sum can only decrease or stay the same
        # Hence, the minimum possible sum is the sum of all elements
        results.append(sum(A))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()