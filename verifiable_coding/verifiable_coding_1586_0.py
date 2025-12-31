import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    first_row = list(map(int, data[1:]))
    
    result = []
    
    for shift in range(N):
        max_score = 0
        for i in range(N):
            a = first_row[i]
            b = first_row[(i + shift) % N]
            current_score = a + b
            if current_score > max_score:
                max_score = current_score
        result.append(str(max_score))
    
    print(' '.join(result))

if __name__ == '__main__':
    solve()