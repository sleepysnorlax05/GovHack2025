FROM python:3.13-slim

WORKDIR /app

# Install curl and other necessary tools
RUN apt-get update && apt-get install -y curl tesseract-ocr libgl1 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Download Ollama CLI binary (adjust URL as per official Ollama downloads)
RUN curl -Lo /usr/local/bin/ollama https://ollama.com/downloads/ollama-linux-x64 && \
    chmod +x /usr/local/bin/ollama

# Pull lightweight Ollama model during build
RUN ollama pull ollama/gpt-small

# Copy application source code
COPY ./src ./src

# Expose Streamlit default port
EXPOSE 8501

ENV STREAMLIT_SERVER_ENABLECORS=false \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501

# Run Streamlit app
CMD ["streamlit", "run", "src/main.py"]
