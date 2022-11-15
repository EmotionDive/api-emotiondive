# Emotion Dive API
## Installation
** It requires to have [python 3.3+](https://www.python.org/) previously installed
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements of the project.
```bash
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
## Execution
Run the following command.
```bash
flask --app api --debug run
```
Afterwards, just head to http://127.0.0.1:5000/hello for a greeting.
## Documentation
Currently based on the Flask-RESTful documentation. Refer to [Flask-RESTful site](https://flask-restful.readthedocs.io/en/latest/index.html) to learn about the usage in this project.

For info related to flask-sqlalchemy check the [flask-sqlalchemy site](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/).

For info related to flask-marshmallow check the [flask-mashmallow site](https://flask-marshmallow.readthedocs.io/en/latest/).

## Contributing
Don't forget to run the following command if you install some libraries.
```bash
pip freeze > requirements.txt
```
