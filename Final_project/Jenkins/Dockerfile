# start by pulling the python image
FROM python:3.8-alpine

# copy every content from the local file to the image
COPY /Final_project/Jenkins /app

# switch working directory
WORKDIR /app

# install flask
RUN pip install Flask

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["/app/PrintPDF.py" ]
