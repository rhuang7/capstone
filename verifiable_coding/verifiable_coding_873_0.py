import sys
import heapq

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    S_list = data[1:T+1]

    # Define the Petersen graph adjacency list
    adj = {
        0: [1, 2, 3, 4, 5],
        1: [0, 2, 3, 6, 7],
        2: [0, 1, 4, 6, 8],
        3: [0, 1, 5, 7, 8],
        4: [0, 2, 5, 7, 9],
        5: [0, 3, 4, 8, 9],
        6: [1, 2, 7, 8, 9],
        7: [1, 3, 6, 9, 8],
        8: [2, 3, 6, 7, 9],
        9: [4, 5, 6, 7, 8]
    }

    # Mapping from letters to vertices
    letter_to_vertex = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

    def solve():
        for S in S_list:
            n = len(S)
            if n == 0:
                print(-1)
                continue

            # Initialize the priority queue for Dijkstra's algorithm
            # Each element is (current_position, current_vertex, path)
            # We use a priority queue to find the lexicographically smallest path
            # The priority is based on the path string (lex order)
            # We use a heap with tuples (path, current_vertex, current_position)
            heap = []
            # Start from the first character's vertex
            start_vertex = letter_to_vertex[S[0]]
            heapq.heappush(heap, ("" + str(start_vertex), start_vertex, 0))

            # Visited dictionary to keep track of the minimum path to each (vertex, position)
            visited = {}

            while heap:
                path_str, current_vertex, pos = heapq.heappop(heap)
                if pos == n - 1:
                    # We have reached the end of the string
                    print(path_str)
                    break
                if (current_vertex, pos) in visited:
                    if visited[(current_vertex, pos)] <= path_str:
                        continue
                visited[(current_vertex, pos)] = path_str

                # Try to move to the next character
                next_char = S[pos + 1]
                next_vertex = letter_to_vertex[next_char]

                # Try all adjacent vertices
                for neighbor in adj[current_vertex]:
                    new_path = path_str + str(neighbor)
                    if (neighbor, pos + 1) not in visited or new_path < visited[(neighbor, pos + 1)]:
                        heapq.heappush(heap, (new_path, neighbor, pos + 1))
            else:
                # No valid path found
                print(-1)

    if __name__ == '__main__':
        solve()