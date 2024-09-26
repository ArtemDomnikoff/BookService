from concurrent import futures
import os, sys
import grpc
import django


sys.path.append('D:\Python projects\BookService\book_app')  # Укажите полный путь к корневой директории проекта Django

django.setup()

import book_pb2
import book_pb2_grpc
from models import Book


class BookService(book_pb2_grpc.BookServiceServicer):
    def GetBookById(self, request, context):
        book = Book.objects.get(id=request.id)
        return book

    def GetBooks(self, request, context):
        books = Book.objects.all()
        return book_pb2.GetBooksResponse(
            books=books
        )


def serve():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        book_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
        server.add_insecure_port('[::]:50052')
        server.start()
        print("gRPC сервер запущен на порту 50052")
        server.wait_for_termination()
    except Exception as e:
        print(f"Ошибка сервера: {e}")


if __name__ == '__main__':
    serve()
