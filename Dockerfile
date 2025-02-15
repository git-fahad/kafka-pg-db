FROM python:3.9

WORKDIR /app

COPY sales_data.py .
COPY kafka-producer.py .

CMD ["python3", "sales_data.py", "&&", "python3", "kafka-producer.py"]