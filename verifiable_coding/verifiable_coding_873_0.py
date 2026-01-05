import sys
import heapq

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    S_list = data[1:T+1]

    # Define the adjacency list for the Petersen graph
    # Vertices are numbered 0-9
    # Edges are as per the Petersen graph structure
    adj = {
        0: [1, 2, 3, 4],
        1: [0, 5, 6],
        2: [0, 5, 7],
        3: [0, 5, 8],
        4: [0, 5, 9],
        5: [1, 2, 3, 4, 6, 7, 8, 9],
        6: [1, 5, 9],
        7: [2, 5, 8],
        8: [3, 5, 7],
        9: [4, 5, 6]
    }

    # Map letters to vertices
    letter_to_vertex = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4
    }

    # Function to get the lex order of a walk
    def get_lex_order(walk):
        return ''.join(str(v) for v in walk)

    # Function to find the lex smallest walk for a given string S
    def solve_S(S):
        if not S:
            return "0"  # Empty walk

        # Initialize the priority queue for Dijkstra's algorithm
        # Each element is (current_lex_order, current_position, current_vertex)
        # We use a priority queue to always expand the lex smallest path first
        # We also track the visited states to avoid cycles
        # The state is (current_position, current_vertex)
        # We use a dictionary to track the best (lex smallest) path to each state
        from collections import defaultdict
        import heapq

        # Map letters to their corresponding vertex
        letter_to_vertex = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4
        }

        # Initialize the priority queue
        pq = []
        # Start from the vertex corresponding to the first letter
        start_vertex = letter_to_vertex[S[0]]
        # The initial path is just the starting vertex
        initial_path = [start_vertex]
        # The initial lex order is the string representation of the path
        initial_lex_order = get_lex_order(initial_path)
        # Push the initial state into the priority queue
        heapq.heappush(pq, (initial_lex_order, 0, start_vertex))

        # Dictionary to track the best (lex smallest) path to each (position, vertex) state
        # key: (position, vertex), value: (lex_order, path)
        best = {}
        best_key = (0, start_vertex)
        best[best_key] = (initial_lex_order, initial_path)

        # Process the priority queue
        while pq:
            current_lex_order, pos, current_vertex = heapq.heappop(pq)
            # If we've reached the end of the string, return the path
            if pos == len(S):
                return get_lex_order(current_path)
            # Get the next letter
            next_letter = S[pos]
            next_vertex = letter_to_vertex[next_letter]
            # Check if we can move from current_vertex to next_vertex
            if next_vertex in adj[current_vertex]:
                # Create the new path
                new_path = current_path + [next_vertex]
                # Get the new lex order
                new_lex_order = get_lex_order(new_path)
                # Check if this state (pos+1, next_vertex) has been visited with a better path
                state = (pos + 1, next_vertex)
                if state not in best or new_lex_order < best[state][0]:
                    best[state] = (new_lex_order, new_path)
                    heapq.heappush(pq, (new_lex_order, pos + 1, next_vertex))
            # If we can't move, continue with the next state in the priority queue

        # If we exhaust the queue without finding a path, return -1
        return "-1"

    # Process each test case
    for S in S_list:
        result = solve_S(S)
        print(result)

if __name__ == '__main__':
    main()