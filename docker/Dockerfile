# Use a specific version of Python for consistency
FROM python:3.9

# Install dependencies
RUN apt-get update && \
    apt-get install -y build-essential libffi-dev libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Add labels
LABEL Name="Speech to Sign" \
      Author="Nikita" \
      Team="Tech Titans" \
      Source="https://github.com/minikzzie/speechtosign.git"

# Set working directory
WORKDIR /app

# Create and activate a virtual environment
RUN python -m venv /env
ENV PATH="/env/bin:$PATH"

# Copy application code
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000]
