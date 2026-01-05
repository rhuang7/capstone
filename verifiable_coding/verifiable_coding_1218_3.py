import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        X = int(data[index])
        N = int(data[index+1])
        index += 2
        # Find the number of terms in the arithmetic sequence
        count = N // X
        # Sum of arithmetic sequence: (first term + last term) * number of terms // 2
        first_term = X
        last_term = X * count
        salary = (first_term + last_term) * count // 2
        results.append(str(salary))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()