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
    # Based on the standard Petersen graph structure
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

    # For each test case
    for S in S_list:
        # Initialize the priority queue for Dijkstra's algorithm
        # Each element is (current_position, current_letter_index, path)
        # We want the lex smallest path, so we prioritize by the path string
        # We use a priority queue with tuples (path, current_position, current_letter_index)
        # The priority is based on the path string (lex order)
        pq = []
        # Start from the vertex corresponding to the first letter
        start_vertex = letter_to_vertex[S[0]]
        # Initial path is just the start vertex as a string
        initial_path = str(start_vertex)
        # Push the initial state into the priority queue
        heapq.heappush(pq, (initial_path, start_vertex, 0))

        # To track visited states (vertex, letter index)
        visited = set()
        visited.add((start_vertex, 0))

        found = False
        result = ""

        while pq:
            path, current_vertex, current_index = heapq.heappop(pq)
            # If we have reached the end of the string
            if current_index == len(S):
                result = path
                found = True
                break
            # Get the next letter
            next_letter = S[current_index]
            # Get the next vertex corresponding to the letter
            next_vertex = letter_to_vertex[next_letter]
            # Check if we can move from current_vertex to next_vertex
            if next_vertex in adj[current_vertex]:
                # Create the new path
                new_path = path + str(next_vertex)
                # Check if this state has been visited
                if (next_vertex, current_index + 1) not in visited:
                    visited.add((next_vertex, current_index + 1))
                    heapq.heappush(pq, (new_path, next_vertex, current_index + 1))

        if found:
            print(result)
        else:
            print(-1)

if __name__ == '__main__':
    main()