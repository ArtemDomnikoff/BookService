FROM python:3.9
WORKDIR /book_app
COPY . /book_app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
