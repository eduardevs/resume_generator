FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that FastAPI will run on (usually 8000 for development)
EXPOSE 80

# Run Uvicorn with the --reload flag for hot reload in development
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
