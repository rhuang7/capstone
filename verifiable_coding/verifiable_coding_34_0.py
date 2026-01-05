import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    segment_counts = [2, 3, 4, 5, 4, 5, 3, 3, 6, 6]
    
    for n in cases:
        if n == 2:
            print("1")
        else:
            max_digits = n // 2
            if n % 2 == 1:
                max_digits += 1
            print('1' * max_digits)
    
if __name__ == '__main__':
    solve()