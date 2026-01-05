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
    # Then remove it from the list and update the positions
    # Since N is small (<=4000), we can afford to do this efficiently
    # by using a list and removing elements
    
    # Create a list of books for easier manipulation
    book_list = books.copy()
    
    for i in range(N):
        pos = queries[i]
        # Find the book at the given position
        book = book_list[pos - 1]
        # Remove the book from the list
        book_list.pop(pos - 1)
        # Print the book
        print(book)
        
if __name__ == '__main__':
    solve()