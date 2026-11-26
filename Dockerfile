FROM python:slim

WORKDIR /app

COPY pyproject.toml /app/

RUN pip install .

COPY /src/. /app/

CMD ["python", "./main.py"]