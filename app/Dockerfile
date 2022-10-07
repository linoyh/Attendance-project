# Use an official Python runtime as an image
FROM python:3.7-slim

# The EXPOSE instruction indicates the ports on which a container
EXPOSE 5000

#define the env variables flask use
ENV FLASK_APP=myapp.py
ENV FLASK_RUN_HOST=0.0.0.0

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist
WORKDIR /app

#create a system unpriviliged user for runing my application 1001 = group id and user id
RUN addgroup --system -g 1001 attendance_group && adduser --uid 1001 --system --group attendance_group attendance_user
COPY ./requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN apt update
RUN pip install -r requirements.txt

# Run app.py when the container launches by the unpriviliged user
USER attendance_user
COPY . .
CMD python3 myapp.py



