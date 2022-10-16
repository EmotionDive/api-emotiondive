# Emotion Dive API
## Installation
** It requires to have [python 3.3+](https://www.python.org/) previously installed
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements of the project.
```bash
py -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
```
## Execution
Run the following command.
```bash
flask --app api --debug run
```
Afterwards, just head to http://127.0.0.1:5000/hello for a greeting.
## Documentation
Currently based on the Flask documentation, using an Application Factory. Refer to [Flask site](https://flask.palletsprojects.com/en/2.2.x/tutorial/views/) to learn about the Blueprints and Views that will be used.
## Contributing
Don't forget to run the following command if you install some libraries.
```bash
pip freeze > requirements.txt
```
