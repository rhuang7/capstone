import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    M = int(data[0])
    books = list(map(int, data[1:M+1]))
    N = int(data[M+1])
    queries = list(map(int, data[M+2:M+2+N]))
    
    # Create a dictionary to map book numbers to their current positions
    book_pos = {book: i for i, book in enumerate(books)}
    
    # For each query, find the book at the given position
    # Since the books are removed, we need to simulate the process
    # We'll use a list to keep track of the current books and their positions
    current_books = books.copy()
    
    for q in queries:
        # Find the book at position q-1 (0-based)
        book = current_books[q-1]
        # Remove the book from the list
        current_books.pop(q-1)
        # Output the book
        print(book)
        
if __name__ == '__main__':
    solve()