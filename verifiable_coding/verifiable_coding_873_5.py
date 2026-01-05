import sys
import heapq

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    S_list = data[1:T+1]

    # Define the adjacency list for the Petersen graph
    # Based on the standard Petersen graph structure
    adj = {
        0: [1, 2, 3, 4],
        1: [0, 5, 6],
        2: [0, 5, 7],
        3: [0, 5, 8],
        4: [0, 5, 9],
        5: [1, 2, 3, 4, 6, 7, 8, 9],
        6: [1, 5, 9],
        7: [2, 5, 9],
        8: [3, 5, 9],
        9: [4, 5, 9]
    }

    # Map letters to indices
    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

    def solve():
        for S in S_list:
            n = len(S)
            if n == 0:
                print(-1)
                continue

            # Initialize the priority queue for Dijkstra's algorithm
            # Each element is (current_lex_order, current_position, current_node)
            # Lex order is determined by the string of node numbers
            # We want the lex smallest path, so we use a priority queue
            # We also need to track visited states to avoid cycles
            # State is (position, node)
            visited = set()
            heap = []
            # Start from all possible nodes (0-9) with position 0
            for start_node in range(10):
                # The initial string is just the start node
                # We want the lex smallest, so we start with the smallest node
                # But we need to consider all possibilities
                # We'll use a priority queue to find the lex smallest path
                # The priority is the current string (as a number)
                # We can represent it as a string for comparison
                # But since we need to minimize lex order, we can use a tuple
                # We'll use a priority queue that compares the string as a number
                # We'll use a priority queue with (current_string, position, node)
                # The current_string is the string of node numbers so far
                # We'll use a string to compare lex order
                # We can represent the current string as a string, and compare it lexicographically
                # So we push (current_string, position, node)
                # The initial string is the start node as a string
                current_string = str(start_node)
                heapq.heappush(heap, (current_string, 0, start_node))
                visited.add((0, start_node))

            found = False
            result = ""

            while heap:
                current_string, pos, node = heapq.heappop(heap)
                if pos == n - 1:
                    # We've reached the end of the string
                    # This is a valid walk
                    found = True
                    result = current_string
                    break
                if pos >= n:
                    continue
                # Get the next letter
                next_letter = S[pos]
                next_idx = letter_to_idx[next_letter]
                # Find all neighbors of the current node
                for neighbor in adj[node]:
                    # Check if we can move to this neighbor
                    # The next character in the string should match the letter
                    # We need to check if the next character is correct
                    # The next character is S[pos + 1]
                    if pos + 1 < n:
                        next_char = S[pos + 1]
                        next_char_idx = letter_to_idx[next_char]
                        # Check if the neighbor is connected to the current node
                        # And if the next character is correct
                        # We need to check if the next character is correct
                        # We can only move to the neighbor if the next character is correct
                        # But since we are building the string step by step, we need to check
                        # if the next character is correct
                        # So we need to check if the next character is correct
                        # We can only move to the neighbor if the next character is correct
                        # So we check if the next character is correct
                        if next_char_idx == next_idx:
                            # We can move to this neighbor
                            new_string = current_string + str(neighbor)
                            new_pos = pos + 1
                            new_node = neighbor
                            if (new_pos, new_node) not in visited:
                                visited.add((new_pos, new_node))
                                heapq.heappush(heap, (new_string, new_pos, new_node))
                    else:
                        # We can move to this neighbor as long as the next character is correct
                        # But since we are at the end, we can just move
                        new_string = current_string + str(neighbor)
                        new_pos = pos + 1
                        new_node = neighbor
                        if (new_pos, new_node) not in visited:
                            visited.add((new_pos, new_node))
                            heapq.heappush(heap, (new_string, new_pos, new_node))

            if found:
                print(result)
            else:
                print(-1)

    solve()

if __name__ == '__main__':
    main()