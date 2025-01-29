FROM python:3.12.8-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install mage-ai && \
    rm -rf /tmp/* && \
    rm -rf /var/log/* && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /tmp/* /var/tmp/*

# Start Mage
CMD ["mage", "start"]
