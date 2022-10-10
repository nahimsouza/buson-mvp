# BusOn MVP

Repository for BusOn MVP project.

There are some guidelines to start developing for BusOn MVP project using VS Code.

## Project Setup

### **Required software**

- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/download/)
- [Python 3.10.7](https://www.python.org/downloads/)
  - Additional libraries required: in the requirements file


### 1. Clone [buson-mvp](https://github.com/nahimsouza/buson-mvp) project

Use Git to clone the project repository. It is currently available in the following repository:

* https://github.com/nahimsouza/buson-mvp

### 2. Create a environment

#### Installation (Linux):

- Install Python: sudo apt install python3
- Install Django: pip install Django
- Add django-admin e sqlformat no PATH: `export PATH="$HOME/.local/bin:$PATH"`

#### Installation (Windows)

After install Python, include Python path on System Environment Variable PATH, open cmd and run the follow commands:

 * pip install virtualenv
 * pip install virtualenvwrapper-win
 * To create a virtualenv: `mkvirtualenv ENV_NAME`. For this project, the default is to use BusOn instead of `ENV_NAME`
    * With virtual environment created, navigate to project's root directory (`C:\Projects\buson-mvp`) and run command `setprojectdir .`
        * To activate the virtual environment use `workon ENV_NAME` and to exit use `deactivate`
    * With the virtual environment open, use the command `pip install -r requirements.txt` to install the libraries used by the project

### 3. Visual Studio Code

Open the Visual Studio Code in the project folder.

 * Select the Python environment in the status bar at the bottom of the window
 * Be happy! 😉

## Main Commands:

- Run server: `python3 manage.py runserver`
- Create migrations based on the changes detected to your models: `python3 manage.py makemigrations` 
- Update database based on migrations: `python3 manage.py migrate`
