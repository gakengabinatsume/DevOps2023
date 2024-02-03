# Use an official Python runtime as the base image
#FROM python:3.9-slim
FROM ubuntu
RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask
# Set the working directory in the container
WORKDIR /app

# Copy the Python script and PDF file into the container
COPY /Final_project/Jenkins/PrintPDF.py /app
COPY /Final_project/Jenkins/CV.pdf /app

# Install the required dependencies
#RUN pip install windows
USER root
# Run the Python script when the container starts
#CMD ["python", "/app/PrintPDF.py"]
CMD ["python3","-m","flask","run","--host=0.0.0.0"]
