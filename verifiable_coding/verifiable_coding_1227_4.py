import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        colors = input[idx:idx+6]
        idx += 6
        front, back, left, right, top, bottom = colors
        # Check all combinations of three sides that are pairwise adjacent
        # Adjacent pairs are: (front, left), (front, right), (front, top), (front, bottom),
        # (back, left), (back, right), (back, top), (back, bottom),
        # (left, top), (left, bottom), (right, top), (right, bottom),
        # (top, left), (top, right), (top, front), (top, back),
        # (bottom, left), (bottom, right), (bottom, front), (bottom, back)
        # But we need to check triplets where all three are pairwise adjacent
        # So check all combinations of three sides that are pairwise adjacent
        # The valid triplets are:
        # (front, left, top), (front, left, bottom), (front, right, top), (front, right, bottom),
        # (back, left, top), (back, left, bottom), (back, right, top), (back, right, bottom),
        # (left, top, bottom), (right, top, bottom)
        # Check if any of these triplets have all three colors the same
        if (front == left == top or
            front == left == bottom or
            front == right == top or
            front == right == bottom or
            back == left == top or
            back == left == bottom or
            back == right == top or
            back == right == bottom or
            left == top == bottom or
            right == top == bottom):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()