import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def game(s):
        # Convert the string into a list of groups of consecutive same characters
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

        # Now simulate the game
        # We'll keep track of the total 1s taken by Alice and Bob
        alice = 0
        bob = 0
        # We'll use a stack to simulate the game
        stack = []
        for char, count in groups:
            # Push the group onto the stack
            stack.append((char, count))
            # Check if the top two groups are the same and can be merged
            while len(stack) >= 2:
                top = stack[-1]
                second = stack[-2]
                if top[0] == second[0]:
                    # Merge the two groups
                    new_char = top[0]
                    new_count = top[1] + second[1]
                    stack.pop()
                    stack.pop()
                    stack.append((new_char, new_count))
                else:
                    break

        # Now simulate the game by taking turns
        # We'll use a list to represent the current groups
        current = groups
        turn = 0  # 0 for Alice, 1 for Bob
        while current:
            # Find all possible moves
            possible_moves = []
            for i in range(len(current)):
                char, count = current[i]
                if char == '1':
                    possible_moves.append((i, count))
            if not possible_moves:
                break
            # Choose the best move (maximize the number of 1s taken)
            # For this problem, we assume that the optimal strategy is to take the largest possible group of 1s
            best_move = None
            best_count = 0
            for i, count in possible_moves:
                if count > best_count:
                    best_count = count
                    best_move = i
            # Take the best move
            char, count = current[best_move]
            if char == '1':
                if turn == 0:
                    alice += count
                else:
                    bob += count
            # Remove the group and merge with neighbors if possible
            del current[best_move]
            # Check if the group before and after can be merged
            if best_move > 0:
                prev_char, prev_count = current[best_move - 1]
                if prev_char == char:
                    new_char = prev_char
                    new_count = prev_count + count
                    current[best_move - 1] = (new_char, new_count)
                    del current[best_move]
            if best_move < len(current) - 1:
                next_char, next_count = current[best_move]
                if next_char == char:
                    new_char = next_char
                    new_count = next_count + count
                    current[best_move] = (new_char, new_count)
                    del current[best_move + 1]
            # Switch turn
            turn = 1 - turn
        return alice

    for s in cases:
        print(game(s))

if __name__ == '__main__':
    solve()