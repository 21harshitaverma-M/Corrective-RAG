FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/
COPY results/ ./results/
COPY README.md .

CMD ["python", "src/test_end_to_end.py"]