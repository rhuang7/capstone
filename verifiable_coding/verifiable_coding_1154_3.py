import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    friends = list(map(int, input[1:n+1]))
    game = list(map(int, input[n+1:]))
    
    from collections import Counter
    friend_count = Counter(friends)
    game_count = Counter(game)
    
    for num, count in game_count.items():
        if count > friend_count.get(num, 0):
            print(num)
            return

if __name__ == '__main__':
    solve()