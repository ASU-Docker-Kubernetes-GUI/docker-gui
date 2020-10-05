FROM python

# Changing working directory to project
WORKDIR /project
ADD . /project

# installing pip requirements
RUN pip install -r requirements.txt

# Run the app
CMD ["python", "app.py"]
