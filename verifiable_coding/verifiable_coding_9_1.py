import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for s in cases:
        # Convert the string to a list of characters
        chars = list(s)
        # Group consecutive characters
        groups = []
        i = 0
        while i < len(chars):
            current = chars[i]
            j = i
            while j < len(chars) and chars[j] == current:
                j += 1
            groups.append((current, j - i))
            i = j

        # Calculate the total number of 1s
        total_ones = sum(count for char, count in groups if char == '1')
        # The game is about taking turns to remove groups of 1s
        # Each player wants to maximize their own score
        # The optimal strategy is to take the largest group of 1s on their turn
        # So we sort the groups of 1s in descending order and alternate taking them
        ones_groups = sorted((count for char, count in groups if char == '1'), reverse=True)
        alice_score = 0
        for i in range(len(ones_groups)):
            if i % 2 == 0:
                alice_score += ones_groups[i]
        print(alice_score)

if __name__ == '__main__':
    solve()