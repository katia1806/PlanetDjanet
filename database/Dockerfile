# define the base image
FROM mongo:latest

ADD requirements.txt .
RUN pip install -r requirements.txt

# use the port number
EXPOSE 27017

# run the command
CMD ["mongod"]
