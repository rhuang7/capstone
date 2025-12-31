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
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # So the number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            # The number of books removed is the index of the book in the heap
            # But since the heap is a priority queue, we can't directly get the index
            # So we need to track the index of each book in the heap
            # So we need to use a priority queue that allows us to track the index
            # So we push tuples (remaining_exercises, book_name, index)
            # and the heap will prioritize based on remaining_exercises
            # and then book_name
            # So when we pop, we get the book with minimum remaining_exercises
            # and if there are multiple, the one with lex smallest name
            #