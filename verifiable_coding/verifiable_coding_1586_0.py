import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    first_row = list(map(int, data[1:]))
    
    result = []
    for k in range(N):
        second_row = first_row[k:] + first_row[:k]
        max_score = 0
        for i in range(N):
            current_score = first_row[i] + second_row[i]
            if current_score > max_score:
                max_score = current_score
        result.append(str(max_score))
    print(' '.join(result))

if __name__ == '__main__':
    solve()