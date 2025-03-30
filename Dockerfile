#Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker's layer caching
COPY requirements.txt /app/

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your application code
COPY . /app/

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Run the Flask app
CMD ["python", "game.py"]
