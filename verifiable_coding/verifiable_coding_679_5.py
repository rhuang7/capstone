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
            # Pop the book with minimum remaining exercises
            # and least number of books to remove
            # The heap is a min-heap based on remaining exercises
            # and then on the book name (lexicographical order)
            # So we can push tuples (remaining_exercises, book_name)
            # and the heap will work as required
            # Pop the minimum
            remaining, name = heapq.heappop(heap)
            print(f"{0} {name.decode()}")
            idx += 1
        else:
            # Add book to the pile
            remaining = int(data[idx])
            name = data[idx+1].decode()
            heapq.heappush(heap, (remaining, name))
            idx += 2

if __name__ == '__main__':
    solve()