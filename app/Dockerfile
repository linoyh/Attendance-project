# Use an official Python runtime as an image
FROM python:3.7-slim
ENTRYPOINT [ "/bin/bash", "-l", "-c" ]

#define the env variables flask use
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Sets the working directory for following COPY and CMD instructions
# creates a directory with this name if it doesn’t exist
WORKDIR /app

#create a system unpriviliged user for runing my application 1001 = group id and user id
RUN apt-get update -y && apt-get install build-essential -y && apt-get install apt-utils -y && apt-get install libmariadb-dev -y && apt-get install libmariadb-dev-compat -y
RUN addgroup --system --gid 1001 attendance_group && adduser --system --uid 1002 attendance_user --gid 1001
USER attendance_user
COPY ./requirements.txt requirements.txt
#RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# The EXPOSE instruction indicates the ports on which a container
EXPOSE 5000

# Run app.py when the container launches by the unpriviliged user
USER root
CMD ["chmod", "u+x", "*.py"]
USER attendance_user
COPY . .
CMD [ "python3", "-m", "flask", "run"]
#CMD python3 app.py



