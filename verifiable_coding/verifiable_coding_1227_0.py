import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        colors = input[idx:idx+6]
        idx += 6
        front, back, left, right, top, bottom = colors
        # Check all possible triplets of adjacent sides
        # Adjacent sides are: front with left, right, top, bottom
        # back with left, right, top, bottom
        # left with front, back, top, bottom
        # right with front, back, top, bottom
        # top with front, back, left, right
        # bottom with front, back, left, right
        # Check all combinations of three adjacent sides
        # Check if any three have the same color
        if (front == left == top or
            front == left == bottom or
            front == right == top or
            front == right == bottom or
            front == top == bottom or
            front == left == right or
            back == left == top or
            back == left == bottom or
            back == right == top or
            back == right == bottom or
            back == top == bottom or
            back == left == right or
            left == right == top or
            left == right == bottom or
            left == top == bottom or
            left == right == back or
            right == top == bottom or
            right == top == back or
            right == bottom == back or
            top == bottom == back or
            top == left == right or
            top == left == back or
            top == right == back or
            bottom == left == right or
            bottom == left == back or
            bottom == right == back):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()