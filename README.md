[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

### Bookstore emulator

Small web application with API for practicing requests

#### Usage

The application require Python version 3.10 or older and Poetry. In order to install the application on your local machine go through the following steps:
1. clone the repo using comand
 ```
git clone https://github.com/ADv0rnik/request-emulator.git
 ```
2. Install and activate virtual environment.
For UNIX-based systems:
```commandline
   python -m venv venv
   source venv/bin/activate
```
3. Run installation of dependencies `poetry install` 
4. Run command `source aliases`
5. Run command `run_emulator`

The docker will run the `start_app.sh` script. While running the application for first time, make sure that `LOAD_FIXTURE` flag is set to `True`. This will allow to upload an initial data into database.