# Time Tracking Server

This repository contains a little demonstration.
It contains an api-server that handles employee working time data.
To run this you need python>=3.13


## Installation
First clone the repo
```bash
git clone https://github.com/MarcBrueck/time_tracking.git
```

If you dont have uv installed, you can install it using pip:
```bash
pip install uv
```
Then create a virtual environment and install the dependencies using uv.
```bash
uv sync
```

Then activate the virtual environment:
```bash
source .venv/bin/activate
```

Create a .env file for storing the env variables outside of git 
```bash
touch .env
```

and then add the necessary env variables, here we only need the database connection. 
Here I decided to use sqlite, because it is the easiest to set up, It can be easily switched to a any of the rdbms like postgres, since we
are using sqlalchemy.

```.env
CONNECTION_STRING="sqlite:///time_tracking.db"
```


## Running the application

You can run the api server using:
```bash
uvicorn time_tracking.main:app --host 127.0.0.1 --port 8000
```
Then you can see the swagger UI listing the api documentation here:
```url
http://127.0.0.1:8000/docs
```

There you can see all the endpoints and paths for example
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/employees/' \
  -H 'accept: application/json'
```
to fetch all employee data

There is also a script that fills the database with some random data:
```bash
python scripts/fill_database.py
```

## Run the application using Docker
First build the image
```bash
docker build -t time_tracking:v1 .
```

and then run it
```bash
docker run -p 8000:8000 -e CONNECTION_STRING="sqlite:///time_tracking.db" time_tracking:v1
```


## Run the unittests
```bash
pytest
```