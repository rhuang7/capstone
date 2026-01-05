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

    # Function to get the lexicographically smallest walk
    def solve(S):
        if len(S) == 0:
            return "0"
        # Initialize the starting vertex based on the first character
        start = letter_to_vertex[S[0]]
        # Priority queue for Dijkstra's algorithm: (current_position, current_path, current_letter_index)
        # We use a priority queue to always choose the lexicographically smallest path
        # The priority is based on the current path string (lex order)
        heap = [(start, str(start), 0)]
        # Visited set to avoid revisiting the same state (vertex, letter index)
        visited = set()
        # The minimum path for each (vertex, letter index)
        min_path = {}

        while heap:
            current_vertex, current_path, current_letter_index = heapq.heappop(heap)
            if current_letter_index == len(S):
                return current_path
            if (current_vertex, current_letter_index) in visited:
                continue
            visited.add((current_vertex, current_letter_index))
            # Get the next letter
            next_letter = S[current_letter_index]
            next_vertex = letter_to_vertex[next_letter]
            # Check if next_vertex is adjacent to current_vertex
            if next_vertex in adj[current_vertex]:
                new_path = current_path + str(next_vertex)
                new_letter_index = current_letter_index + 1
                if (next_vertex, new_letter_index) not in min_path or new_path < min_path[(next_vertex, new_letter_index)]:
                    min_path[(next_vertex, new_letter_index)] = new_path
                    heapq.heappush(heap, (next_vertex, new_path, new_letter_index))
        return "-1"

    for S in S_list:
        result = solve(S)
        print(result)

if __name__ == '__main__':
    main()