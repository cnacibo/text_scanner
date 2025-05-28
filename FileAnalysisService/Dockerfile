FROM python:3.10-slim

LABEL description="FileAnalysisService Dockerfile"

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install --index-url https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "app.main"]

