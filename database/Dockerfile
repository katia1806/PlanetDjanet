# define the base image
FROM mongo:latest


# copy the files to the container
COPY ./files/* /data/
COPY ./mongo-init.sh /docker-entrypoint-initdb.d/

# use the port number
EXPOSE 27017

# run the command
CMD ["mongod"]
