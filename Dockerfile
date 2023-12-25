FROM python:3.8-alpine
COPY ./ app
WORKDIR ./app

RUN pip install -r requirements.txt
# Make port 5000 available to the world outside this container
EXPOSE 5000
# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]


