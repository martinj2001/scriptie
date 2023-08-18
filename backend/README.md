# Running the backend

To run the backend first create a virtual environment with:
```
virtualenv env
```

The use the virtual environment by:
```
source env/bin/activate
```

Now you can install all necessary packages by:
```
pip3 install -r requirements.txt
```

After the installation is finished, run:
```
uvicorn main:app -reload
```