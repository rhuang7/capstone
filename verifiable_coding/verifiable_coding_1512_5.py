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
        # The game is equivalent to a Nim game with two piles
        # The number of moves up is (N - 1) and the number of moves right is (M - 1)
        # Each move can reduce the up count by 1, 2, or 3, and the right count by 1 or 2
        # The Grundy number for up is (N - 1) % 4
        # The Grundy number for right is (M - 1) % 3
        # The XOR of these two gives the outcome
        g_up = (N - 1) % 4
        g_right = (M - 1) % 3
        if (g_up ^ g_right) != 0:
            print("Tuzik")
        else:
            print("Vanya")

if __name__ == '__main__':
    solve()