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
            # Pop from heap
            rem, name = heapq.heappop(heap)
            print(f"{0} {name.decode()}")
            idx += 1
        else:
            # Add book to pile
            rem = int(data[idx])
            name = data[idx + 1].decode()
            heapq.heappush(heap, (rem, name))
            idx += 2

if __name__ == '__main__':
    solve()