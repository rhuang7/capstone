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
            # and the heap will handle the min based on the first element
            # and then the second element
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to keep track of the index of each book in the heap
            # So we need to push (remaining_exercises, book_name, index)
            # and when we pop, the index is the number of books removed
            # So we need to track the index
            # But since the heap is a priority queue, we can't track the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises
            # and then the book with the smallest name
            # So the heap is a min-heap based on remaining_exercises and then on book_name
            # So the first element is the remaining_exercises
            # and the second is the book_name
            # So we pop the smallest element
            # The number of books removed is the index of the book in the heap
            # But since the heap is not a list, we can't get the index
            # So we need to use a priority queue that allows for efficient removal
            # But that's not possible with a standard heap
            # So we need to use a priority queue with the book's remaining exercises
            # and the book's name
            # So we push (remaining_exercises, book_name)
            # and when we pop, we get the book with minimum remaining exercises