import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1

    heap = []
    for _ in range(N):
        action = int(data[idx])
        idx += 1
        if action == -1:
            if not heap:
                print("0")
                print(data[idx])
                idx += 1
                continue
            # Find the book with minimum exercises and least removals
            min_exercises = None
            min_removals = None
            min_name = None
            for i in range(len(heap)):
                if heap[i][0] < min_exercises or (heap[i][0] == min_exercises and i < min_removals):
                    min_exercises = heap[i][0]
                    min_removals = i
                    min_name = heap[i][1]
            print(f"{min_removals} {min_name}")
            # Remove the book from the heap
            del heap[min_removals]
        else:
            book_name = data[idx]
            idx += 1
            heapq.heappush(heap, (action, book_name))

if __name__ == '__main__':
    solve()