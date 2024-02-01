FROM ubuntu:latest

# Install necessary dependencies
RUN apt-get update && apt-get install -y mupdf

# Copy the PDF file into the container
COPY CV.pdf /app

# Set the working directory
WORKDIR /app

# Expose the necessary port
EXPOSE 5000

# Start the PDF viewer
CMD ["mupdf-gl", "CV.pdf"]
