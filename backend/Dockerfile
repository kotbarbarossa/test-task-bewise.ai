FROM python:3.10-slim
WORKDIR /backend
COPY requirements.txt .
RUN pip3 install -r ./requirements.txt --no-cache-dir
COPY . ./
CMD ["gunicorn", "quiz.wsgi:application", "--bind", "0:8000" ]