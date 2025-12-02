FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Base directory for YAML files inside the container
ENV BASE_DIR=/data
ENV FLASK_APP=yaml_parser.app

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]