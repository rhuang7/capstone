import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    x_list = list(map(int, data[1:t+1]))
    
    def is_possible(x):
        if x < 1:
            return False
        # For a single die, the visible pips are 5 (top) + 4 (bottom) + 4 (sides) = 13
        # For a tower of n dice, the visible pips are:
        # - Top face of top die: 1 to 6
        # - Bottom face of bottom die: 1 to 6 (not visible)
        # - For each die in between, the bottom face is not visible, and the top face is not visible
        # - The four side faces of each die (north, south, east, west) are visible
        # For each die, the sum of the four side faces is 14 (since 1+2+3+4+5+6 = 21, and the sum of the opposite faces is 7)
        # So, for each die, the four side faces sum to 14 - (top + bottom)
        # The minimum sum of four side faces is 14 - (6 + 1) = 7
        # The maximum sum of four side faces is 14 - (1 + 6) = 7
        # Wait, this is incorrect. The four side faces are the four faces that are not top or bottom. For a die, the sum of all six faces is 21. If the top and bottom are a and b, then the sum of the four side faces is 21 - a - b. The minimum sum is 21 - 6 - 1 = 14, and the maximum is 21 - 1 - 6 = 14. So for each die, the four side faces sum to 14.
        # So for n dice, the visible pips are:
        # - Top face of top die: 1 to 6
        # - For each die in between, the bottom face is not visible, and the top face is not visible
        # - For each die, the four side faces sum to 14
        # - Bottom face of bottom die is not visible
        # So total visible pips = top_face + (n-1)*14
        # So the total visible pips is top_face + 14*(n-1)
        # So for a given x, we need to find if there exists an n >= 1 and a top_face (1-6) such that x = top_face + 14*(n-1)
        # Rearranging, x - top_face must be divisible by 14 and the result must be >= 0
        # So for each x, check if x - top_face is divisible by 14 and >= 0 for some top_face in 1-6
        for top_face in range(1, 7):
            if (x - top_face) % 14 == 0 and (x - top_face) >= 0:
                return True
        return False
    
    for x in x_list:
        if is_possible(x):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()