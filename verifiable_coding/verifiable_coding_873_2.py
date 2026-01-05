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
    # Edges are as follows (based on the Petersen graph structure):
    # 0 connected to 1, 2, 5
    # 1 connected to 0, 3, 4
    # 2 connected to 0, 3, 6
    # 3 connected to 1, 2, 7
    # 4 connected to 1, 5, 8
    # 5 connected to 0, 4, 6
    # 6 connected to 2, 5, 7
    # 7 connected to 3, 6, 8
    # 8 connected to 4, 7, 9
    # 9 connected to 8, 6
    adj = {
        0: [1, 2, 5],
        1: [0, 3, 4],
        2: [0, 3, 6],
        3: [1, 2, 7],
        4: [1, 5, 8],
        5: [0, 4, 6],
        6: [2, 5, 7],
        7: [3, 6, 8],
        8: [4, 7, 9],
        9: [8, 6]
    }

    # Mapping from letters to vertices (A=0, B=1, C=2, D=3, E=4)
    letter_to_vertex = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

    def solve(S):
        if len(S) == 0:
            return "0"
        # Initialize the priority queue for Dijkstra's algorithm
        # Each element is (current_position, current_path, current_letter_index)
        # We use a priority queue based on the lexicographical order of the path
        # The priority is the path string (lexicographical order)
        # We also track visited states to avoid cycles
        # The state is (current_position, current_letter_index)
        # We use a dictionary to track the minimum path for each state
        from collections import defaultdict
        import heapq

        # Priority queue
        pq = []
        # Start with the first letter
        start_vertex = letter_to_vertex[S[0]]
        heapq.heappush(pq, (start_vertex, [str(start_vertex)], 0))
        # Visited dictionary to track the minimum path for each (vertex, index) state
        visited = dict()
        visited[(start_vertex, 0)] = [str(start_vertex)]

        while pq:
            current_vertex, path, index = heapq.heappop(pq)
            if index == len(S):
                return ''.join(path)
            # Get the next letter
            next_letter = S[index]
            next_vertex = letter_to_vertex[next_letter]
            # Try all neighbors of current_vertex
            for neighbor in adj[current_vertex]:
                # Check if we can move to neighbor
                # The next index is index + 1
                next_index = index + 1
                # Check if we have already visited this state with a better path
                state = (neighbor, next_index)
                if state not in visited or len(visited[state]) > len(path) + 1:
                    new_path = path + [str(neighbor)]
                    visited[state] = new_path
                    heapq.heappush(pq, (neighbor, new_path, next_index))
        # If no path is found
        return "-1"

    for S in S_list:
        result = solve(S)
        print(result)

if __name__ == '__main__':
    main()