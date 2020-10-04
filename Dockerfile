# Download ubuntu 16.04
FROM python:3.6.1-alpine

WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt

# Run the app
CMD ["python", "app.py"]