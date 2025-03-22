FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-kafka.sh .
RUN chmod +x wait-for-kafka.sh

EXPOSE 5000
CMD ["./wait-for-kafka.sh"]
