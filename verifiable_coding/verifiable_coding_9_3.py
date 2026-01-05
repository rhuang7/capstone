import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for s in cases:
        # Group consecutive characters
        groups = []
        prev = s[0]
        count = 1
        for c in s[1:]:
            if c == prev:
                count += 1
            else:
                groups.append((prev, count))
                prev = c
                count = 1
        groups.append((prev, count))

        # Calculate the total number of 1s
        total_ones = sum(count for (ch, count) in groups if ch == '1')
        # Calculate the score for Alice
        alice_score = 0
        turn = 0  # 0 for Alice, 1 for Bob
        for ch, count in groups:
            if ch == '1':
                if turn == 0:
                    alice_score += count
                turn = 1 - turn
        print(alice_score)

if __name__ == '__main__':
    solve()