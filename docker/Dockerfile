FROM python:3

# Install any dependencies you need
RUN apt-get update && apt-get install -y build-essential libffi-dev libpq-dev && rm -rf /var/lib/apt/lists/*

# Labels
LABEL Name= "Speech to sign"
LABEL Author= "Nikita"
LABEL Team= "Tech titans"
LABEL Source= "https://github.com/minikzzie/speechtosign.git"


# Copy your application code
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Command to run your application
CMD ["python", "manage.py", "runserver"]
