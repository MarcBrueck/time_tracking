# Time Tracking Server

This repository contains a little demonstration.
It contains an api-server that handles employee working time data.



## Installation
First clone the repo
```bash
git clone https://some-url
```

Then create a virtual environment and install the dependencies using 
```bash
uv sync
```

Then activate it:
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

There is also a script that fills the database with some random data:
```bash
python scripts/fill_database.py
```