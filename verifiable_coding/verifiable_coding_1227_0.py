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
        # Adjacent sides are: front with left, right, top, bottom
        # back with left, right, top, bottom
        # left with front, back, top, bottom
        # right with front, back, top, bottom
        # top with front, back, left, right
        # bottom with front, back, left, right
        # Check all possible triplets of adjacent sides
        # Check if any three sides have the same color
        if (front == left and front == right and front == top and front == bottom) or \
           (front == left and front == right and front == top and front == back) or \
           (front == left and front == right and front == bottom and front == back) or \
           (front == left and front == top and front == bottom and front == back) or \
           (front == right and front == top and front == bottom and front == back) or \
           (left == right and left == top and left == bottom and left == back) or \
           (left == right and left == top and left == bottom and left == front) or \
           (left == right and left == top and left == back and left == front) or \
           (left == right and left == bottom and left == back and left == front) or \
           (left == top and left == bottom and left == back and left == front) or \
           (left == top and left == bottom and left == back and left == right) or \
           (left == top and left == back and left == front and left == right) or \
           (left == bottom and left == back and left == front and left == right) or \
           (right == top and right == bottom and right == back and right == front) or \
           (right == top and right == bottom and right == back and right == left) or \
           (right == top and right == back and right == front and right == left) or \
           (right == bottom and right == back and right == front and right == left) or \
           (top == bottom and top == back and top == front and top == left) or \
           (top == bottom and top == back and top == front and top == right) or \
           (top == back and top == front and top == left and top == right) or \
           (top == bottom and top == front and top == left and top == right) or \
           (top == back and top == front and top == left and top == right) or \
           (bottom == back and bottom == front and bottom == left and bottom == right) or \
           (bottom == back and bottom == front and bottom == left and bottom == right) or \
           (bottom == back and bottom == left and bottom == right and bottom == front) or \
           (bottom == front and bottom == left and bottom == right and bottom == back) or \
           (bottom == back and bottom == left and bottom == right and bottom == front) or \
           (back == front and back == left and back == right and back == top) or \
           (back == front and back == left and back == right and back == bottom) or \
           (back == left and back == right and back == top and back == bottom) or \
           (back == left and back == right and back == top and back == front) or \
           (back == left and back == top and back == bottom and back == front) or \
           (back == right and back == top and back == bottom and back == front) or \
           (back == left and back == top and back == bottom and back == right) or \
           (back == right and back == top and back == bottom and back == left) or \
           (back == left and back == top and back == bottom and back == right) or \
           (back == right and back == top and back == bottom and back == left) or \
           (back == left and back == top and back == bottom and back == right) or \
           (back == right and back == top and back == bottom and back == left):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()