# Use official Python slim image as base
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /.

# Copy dependency files first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all source code into container
COPY ./src ./src

# Expose port Streamlit listens on by default
EXPOSE 8501

# Set environment variables for Streamlit to run in container
ENV STREAMLIT_SERVER_ENABLECORS=false \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501

# Command to run your app 
CMD ["streamlit", "run", "src/main.py"]
