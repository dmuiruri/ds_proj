# Dockerfile for flask web api

FROM ubuntu:16.04 

# refresh repository
RUN apt-get update 

# install python 3.6
# https://docs.python-guide.org/starting/install3/linux/
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.6
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip


# install packages
RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip3 install flask_swagger
RUN pip3 install flask_swagger_ui
RUN pip3 install flask-cors
RUN pip3 install pandas
RUN pip3 install -U statsmodels
RUN pip3 install scipy
RUN pip3 install sklearn


COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]

EXPOSE 5000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DOCKER_ENV=true

# CMD is executed after docker run
CMD ["app.py"]
