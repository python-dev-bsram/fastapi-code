# Use the official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY fastapi-pytest/requirements.txt .

# Install dependencies
RUN pip install -r --no-cache-dir requirements.txt

# Copy the rest of the app's code
COPY fastapi-pytest/ .

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
