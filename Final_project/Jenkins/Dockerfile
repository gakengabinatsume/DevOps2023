# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and PDF file into the container
COPY PrintPDF.py /app
COPY CV.pdf /app

# Install the required dependencies
RUN pip install PyPDF2

# Run the Python script when the container starts
CMD ["python", "/app/PrintPDF.py"]
