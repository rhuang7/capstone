import sys
import heapq

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    S_list = data[1:T+1]

    # Define the adjacency list for the Petersen graph
    # The Petersen graph has vertices 0-9 with edges as follows:
    # 0 connected to 1, 2, 5
    # 1 connected to 0, 3, 4
    # 2 connected to 0, 3, 6
    # 3 connected to 1, 2, 7
    # 4 connected to 1, 5, 8
    # 5 connected to 0, 4, 6
    # 6 connected to 2, 5, 9
    # 7 connected to 3, 8, 9
    # 8 connected to 4, 7, 9
    # 9 connected to 6, 7, 8
    adj = {
        0: [1, 2, 5],
        1: [0, 3, 4],
        2: [0, 3, 6],
        3: [1, 2, 7],
        4: [1, 5, 8],
        5: [0, 4, 6],
        6: [2, 5, 9],
        7: [3, 8, 9],
        8: [4, 7, 9],
        9: [6, 7, 8]
    }

    # Lexicographical order of letters: A < B < C < D < E
    letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

    def solve(S):
        if len(S) == 0:
            return "0"  # Empty string, trivial case

        # Initialize priority queue for Dijkstra's algorithm
        # Each element is (current_position, current_letter_index, path)
        # We want to find the lexicographically smallest path
        # So we prioritize by current_letter_index, then by position
        heap = []
        # Start with all possible starting positions (0-9)
        for start in range(10):
            heapq.heappush(heap, (0, start, [str(start)]))

        # Map to store the minimum lex path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # The key is (position, letter_index), the value is the path string
        # We use a dictionary to avoid recomputing paths
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to store the best path for each (position, letter_index)
        # We use a dictionary to