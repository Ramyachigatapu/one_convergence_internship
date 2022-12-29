FROM python:3.8

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install Flask

# copy every content from the local file to the image
COPY . /app



CMD ["python3", "app.py" ]

