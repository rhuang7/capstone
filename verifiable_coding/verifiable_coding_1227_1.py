import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        colors = input[idx:idx+6]
        idx += 6
        # Check all possible triplets of adjacent sides
        # Adjacent sides are: (front, left, top), (front, right, top), (front, left, bottom), (front, right, bottom), (back, left, top), (back, right, top), (back, left, bottom), (back, right, bottom)
        # Also check (top, left, front), (top, right, front), (top, left, back), (top, right, back), (bottom, left, front), (bottom, right, front), (bottom, left, back), (bottom, right, back)
        # But since we need three pairwise adjacent sides, we can check all combinations of three sides that are pairwise adjacent
        # The possible triplets are:
        # (front, left, top), (front, left, bottom), (front, right, top), (front, right, bottom), (back, left, top), (back, left, bottom), (back, right, top), (back, right, bottom)
        # Also (top, left, front), (top, right, front), (top, left, back), (top, right, back), (bottom, left, front), (bottom, right, front), (bottom, left, back), (bottom, right, back)
        # But since the order is fixed, we can check the following 8 triplets:
        triplets = [
            (0, 2, 4), (0, 2, 5), (0, 3, 4), (0, 3, 5),
            (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)
        ]
        found = False
        for triplet in triplets:
            a, b, c = triplet
            if colors[a] == colors[b] == colors[c]:
                found = True
                break
        print("YES" if found else "NO")

if __name__ == '__main__':
    solve()