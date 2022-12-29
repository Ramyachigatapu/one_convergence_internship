FROM python:3
WORKDIR /flask
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "./app.py"]
