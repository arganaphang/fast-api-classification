FROM python:3.11.8-slim-bullseye
WORKDIR /application
COPY . .
RUN pip install poetry && poetry install --no-dev
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]