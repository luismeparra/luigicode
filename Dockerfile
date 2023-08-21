# Use a base Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port of your API
EXPOSE 8000

# Set environment variables if necessary
# ENV VARIABLE_NAME=value

# Run the API when the container is started
CMD ["python", "api/app.py"]
