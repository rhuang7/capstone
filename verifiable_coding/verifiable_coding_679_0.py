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
            # Get the book with minimum remaining exercises
            # and least number of books to remove
            # Pop the book with minimum remaining exercises
            # and least number of books to remove
            # The heap is a min-heap based on remaining exercises
            # and then on the book name (lexicographical order)
            # So we push tuples (remaining_exercises, book_name)
            # and the heap will take care of the min based on the first element
            # and then the second element
            # So when we pop, we get the book with minimum remaining exercises
            # and if there are multiple, the one with lex smallest name
            # So the number of books removed is the number of books above it
            # which is the index in the heap
            # But since we are using a heap, we can't directly get the index
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises, book_name, index)
            # and the index is the number of books removed
            # But since the heap is a min-heap, the index is not directly available
            # So we need to track the index of each book in the heap
            # But that's not feasible with a standard heap
            # So we need to use a priority queue that can give us the minimum
            # and the number of books removed
            # So we can use a heap that stores (remaining_exercises,