FROM python:3.10-slim

WORKDIR /app

# Install system geospatial and native dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgdal-dev \
    gdal-bin \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 9090

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
