# PlanetDjanet


## For running
### Initialisation
If it is the first time to run this project, please run
```docker-compose up --build```
or run  ```docker-compose up``` if it is not the first time that you run it.

If you have already run our project and you want to Clear the docker, please run
```docker-compose down -v```, but after that please run ```docker-compose up --build```

### Running of the application
Go to the link http://localhost:8501/


## For database
- Dockerfile: Create a Docker container for a MongoDB server with additional Python requirements
- init-mongos.js: Initialise an user of our database planet_djanet
- mongo-init.sh: Put automatically the json, csv file into the collection of MongoDB
- files: Store all the files used to create the database
- github\workflows\process_csv.yml --> Convert all the csv files into uft-8 for each push
- scripts\process_csv.py --> Do the work of converting

