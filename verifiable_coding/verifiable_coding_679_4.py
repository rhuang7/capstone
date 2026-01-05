import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    idx = 1
    heap = []
    for _ in range(N):
        if data[idx] == b'-1':
            # Do book exercise
            # Find the book with minimum remaining exercises
            # and least number of books to remove
            min_val = float('inf')
            min_idx = -1
            for i in range(len(heap)):
                if heap[i][0] < min_val:
                    min_val = heap[i][0]
                    min_idx = i
                elif heap[i][0] == min_val and i < min_idx:
                    min_idx = i
            # Remove books from top to min_idx
            removed = len(heap) - min_idx - 1
            # Remove the book
            del heap[min_idx]
            # Output
            print(f"{removed} {heap[min_idx][1]}")
            idx += 1
        else:
            # Add book to pile
            num = int(data[idx])
            name = data[idx + 1].decode()
            heapq.heappush(heap, (num, name))
            idx += 2

if __name__ == '__main__':
    solve()