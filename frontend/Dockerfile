FROM python:3.9-slim

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . /app

# install dependencies  
RUN pip install -r requirements.txt

# expose port 8501 to the host
EXPOSE 8501

# run the command to start up the server
CMD ["streamlit", "run", "app.py"]