import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    friends = list(map(int, input[1:n+1]))
    game = list(map(int, input[n+1:]))
    
    from collections import defaultdict
    count = defaultdict(int)
    for num in friends:
        count[num] += 1
    for num in game:
        count[num] += 1
    for num in game:
        if count[num] == 1:
            print(num)
            return

if __name__ == '__main__':
    solve()