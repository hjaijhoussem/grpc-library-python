import grpc
from concurrent import futures
import time
import library_pb2
import library_pb2_grpc
from prometheus_client import start_http_server, Counter, Histogram

# Prometheus metrics
grpc_requests = Counter(
    'grpc_requests_total', 
    'Total number of gRPC requests',
    ['method', 'status']
)
grpc_request_duration = Histogram(
    'grpc_request_duration_seconds', 
    'Duration of gRPC requests in seconds',
    ['method']
)
grpc_request_errors = Counter(
    'grpc_request_errors_total', 
    'Total number of gRPC errors',
    ['method']
)

# In-memory storage for books
books = {}

class LibraryService(library_pb2_grpc.LibraryServiceServicer):
    def CreateBook(self, request, context):
        start_time = time.time()
        try:
            book_id = len(books) + 1
            book = library_pb2.Book(id=book_id, title=request.book.title, author=request.book.author, 
                                     isbn=request.book.isbn, publication_year=request.book.publication_year, 
                                     genre=request.book.genre)
            books[book_id] = book
            print(f"Created book: {book}")
            grpc_requests.labels(method='CreateBook', status='success').inc()
            return library_pb2.CreateBookResponse(book=book)
        except Exception as e:
            grpc_request_errors.labels(method='CreateBook').inc()
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return library_pb2.CreateBookResponse()
        finally:
            duration = time.time() - start_time
            grpc_request_duration.labels(method='CreateBook').observe(duration)

    def GetBook(self, request, context):
        start_time = time.time()
        try:
            book = books.get(request.id)
            if book is not None:
                print(f"Retrieved book: {book}")
                grpc_requests.labels(method='GetBook', status='success').inc()
                return library_pb2.GetBookResponse(book=book)
            print(f"Book not found for ID: {request.id}")
            grpc_requests.labels(method='GetBook', status='not_found').inc()
            context.set_details("Book not found.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return library_pb2.GetBookResponse()
        finally:
            duration = time.time() - start_time
            grpc_request_duration.labels(method='GetBook').observe(duration)

    def UpdateBook(self, request, context):
        start_time = time.time()
        try:
            if request.book.id in books:
                books[request.book.id] = request.book
                print(f"Updated book: {request.book}")
                grpc_requests.labels(method='UpdateBook', status='success').inc()
                return library_pb2.UpdateBookResponse(book=request.book)
            print(f"Book not found for ID: {request.book.id}")
            grpc_requests.labels(method='UpdateBook', status='not_found').inc()
            context.set_details("Book not found.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return library_pb2.UpdateBookResponse()
        finally:
            duration = time.time() - start_time
            grpc_request_duration.labels(method='UpdateBook').observe(duration)

    def DeleteBook(self, request, context):
        start_time = time.time()
        try:
            if request.id in books:
                del books[request.id]
                print(f"Deleted book with ID: {request.id}")
                grpc_requests.labels(method='DeleteBook', status='success').inc()
                return library_pb2.DeleteBookResponse(success=True)
            print(f"Book not found for ID: {request.id}")
            grpc_requests.labels(method='DeleteBook', status='not_found').inc()
            context.set_details("Book not found.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return library_pb2.DeleteBookResponse(success=False)
        finally:
            duration = time.time() - start_time
            grpc_request_duration.labels(method='DeleteBook').observe(duration)

    def ListBooks(self, request, context):
        start_time = time.time()
        print("Listing all books:")
        for book in books.values():
            print(book)
        grpc_requests.labels(method='ListBooks', status='success').inc()
        return library_pb2.ListBooksResponse(books=list(books.values()))

def serve():
    # Start Prometheus metrics server
    start_http_server(8000)
    print("Prometheus metrics exposed on port 8000.")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_LibraryServiceServicer_to_server(LibraryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051.")
    try:
        while True:
            time.sleep(86400)  # Keep the server running
    except KeyboardInterrupt:
        print("Server is shutting down.")
        server.stop(0)

if __name__ == '__main__':
    serve()
