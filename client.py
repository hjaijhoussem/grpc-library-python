import grpc
import library_pb2
import library_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = library_pb2_grpc.LibraryServiceStub(channel)

        # Create a book
        book = library_pb2.Book(title="The Great Gatsby", author="F. Scott Fitzgerald",
                                 isbn="9780743273565", publication_year=1925, genre="Fiction")
        response = stub.CreateBook(library_pb2.CreateBookRequest(book=book))
        print("Book created:", response.book)

        # List books
        response = stub.ListBooks(library_pb2.ListBooksRequest())
        print("Books in library:")
        for book in response.books:
            print(f"{book.id}: {book.title} by {book.author}")

        # Get a specific book
        response = stub.GetBook(library_pb2.GetBookRequest(id=1))
        print("Get book:", response.book)

        # Update a book
        book.title = "The Great Gatsby (Updated)"
        response = stub.UpdateBook(library_pb2.UpdateBookRequest(book=book))
        print("Updated book:", response.book)

        # Delete a book
        response = stub.DeleteBook(library_pb2.DeleteBookRequest(id=1))
        print("Deleted book:", response.success)

if __name__ == '__main__':
    run()
