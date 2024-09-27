FROM python:3.9
WORKDIR /book_app
COPY grpc_service /book_app/
RUN pip install -r requirements.txt
CMD ["python", "server.py"]
