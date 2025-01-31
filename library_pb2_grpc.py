# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import library_pb2 as library__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in library_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LibraryServiceStub(object):
    """The Library service defines the CRUD operations for books
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/library.LibraryService/CreateBook',
                request_serializer=library__pb2.CreateBookRequest.SerializeToString,
                response_deserializer=library__pb2.CreateBookResponse.FromString,
                _registered_method=True)
        self.GetBook = channel.unary_unary(
                '/library.LibraryService/GetBook',
                request_serializer=library__pb2.GetBookRequest.SerializeToString,
                response_deserializer=library__pb2.GetBookResponse.FromString,
                _registered_method=True)
        self.UpdateBook = channel.unary_unary(
                '/library.LibraryService/UpdateBook',
                request_serializer=library__pb2.UpdateBookRequest.SerializeToString,
                response_deserializer=library__pb2.UpdateBookResponse.FromString,
                _registered_method=True)
        self.DeleteBook = channel.unary_unary(
                '/library.LibraryService/DeleteBook',
                request_serializer=library__pb2.DeleteBookRequest.SerializeToString,
                response_deserializer=library__pb2.DeleteBookResponse.FromString,
                _registered_method=True)
        self.ListBooks = channel.unary_unary(
                '/library.LibraryService/ListBooks',
                request_serializer=library__pb2.ListBooksRequest.SerializeToString,
                response_deserializer=library__pb2.ListBooksResponse.FromString,
                _registered_method=True)


class LibraryServiceServicer(object):
    """The Library service defines the CRUD operations for books
    """

    def CreateBook(self, request, context):
        """Create a new book
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Get details of a book by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBook(self, request, context):
        """Update an existing book
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBook(self, request, context):
        """Delete a book by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBooks(self, request, context):
        """List all books
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LibraryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=library__pb2.CreateBookRequest.FromString,
                    response_serializer=library__pb2.CreateBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=library__pb2.GetBookRequest.FromString,
                    response_serializer=library__pb2.GetBookResponse.SerializeToString,
            ),
            'UpdateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBook,
                    request_deserializer=library__pb2.UpdateBookRequest.FromString,
                    response_serializer=library__pb2.UpdateBookResponse.SerializeToString,
            ),
            'DeleteBook': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBook,
                    request_deserializer=library__pb2.DeleteBookRequest.FromString,
                    response_serializer=library__pb2.DeleteBookResponse.SerializeToString,
            ),
            'ListBooks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBooks,
                    request_deserializer=library__pb2.ListBooksRequest.FromString,
                    response_serializer=library__pb2.ListBooksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'library.LibraryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('library.LibraryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LibraryService(object):
    """The Library service defines the CRUD operations for books
    """

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/library.LibraryService/CreateBook',
            library__pb2.CreateBookRequest.SerializeToString,
            library__pb2.CreateBookResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/library.LibraryService/GetBook',
            library__pb2.GetBookRequest.SerializeToString,
            library__pb2.GetBookResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/library.LibraryService/UpdateBook',
            library__pb2.UpdateBookRequest.SerializeToString,
            library__pb2.UpdateBookResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/library.LibraryService/DeleteBook',
            library__pb2.DeleteBookRequest.SerializeToString,
            library__pb2.DeleteBookResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListBooks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/library.LibraryService/ListBooks',
            library__pb2.ListBooksRequest.SerializeToString,
            library__pb2.ListBooksResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
