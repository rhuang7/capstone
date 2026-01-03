import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        # Calculate the Grundy numbers for the game
        # The game is a combination of two independent games: moving up and moving right
        # The Grundy number for moving up is (N - 1) % 4
        # The Grundy number for moving right is (M - 1) % 2
        # The total Grundy number is the XOR of the two
        grundy_up = (N - 1) % 4
        grundy_right = (M - 1) % 2
        if grundy_up ^ grundy_right != 0:
            print("Tuzik")
        else:
            print("Vanya")

if __name__ == '__main__':
    solve()