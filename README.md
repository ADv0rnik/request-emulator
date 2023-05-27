[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

### Bookstore emulator

Small REST API based web application for educational purposes 

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

#### Test

1. From root directory run command `run_emulator_test`. This will execute docker compose instructions
2. To check test results run `show_logs`
3. Remove test containers by following command `stop_tests`

#### Deploy to Railway.app

1. Create a PostgreSQL instance in your railway.app account.
   - Copy-paste credentials from railway.app into your .env file 
   - Run command `alembic upgrade head`
   - Run command ```python run_db.py```
2. Create an application instance (choose a GitHub Repo for deploy)
3. Copy and paste variables from .env (Note: host and port for application must be 0.0.0.0 and $PORT respectively, where $PORT - name of variable)
4. Deploy will run automatically triggered by applying changes