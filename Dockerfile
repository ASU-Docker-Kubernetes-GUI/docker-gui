# Using 3.6.1 for now
FROM python:3.6.1-alpine

# Changing working directory to project
WORKDIR /project
ADD . /project

# installing pip requirements
RUN pip install -r requirements.txt

# Change the user to nobody
USER nobody

# Run the app
CMD ["python", "app.py"]
