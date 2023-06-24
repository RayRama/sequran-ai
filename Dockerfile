# Base image
FROM debian:bullseye-slim

# Install dependencies
RUN apt-get update && apt-get install -y git neovim netcat python3-pip

# Copy web service files
COPY main.py /home/sequran-ai/main.py
COPY quran.xlsx /home/sequran-ai/quran.xlsx
COPY requirements.txt /home/sequran-ai/requirements.txt

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /home/sequran-ai/requirements.txt

# Set working directory
WORKDIR /home/sequran-ai

# Expose port
EXPOSE 25117

# Start web service
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "25117"]
