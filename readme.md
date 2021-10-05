# Follow these Steps Carefully
## Commands to run
### Clone
```commandline
git clone https://github.com/nhridoy/TechForing-Ltd.git
```
### Create Virtual Environment
```commandline
py venv -m venv
```
### Activate Virtual Environment (for cmd)
```commandline
cd venv/Scripts/activate
```
### MakeMigrations and Migrate
```commandline
py manage.py makemigrations
```
```commandline
py manage.py migrate
```
### Create SuperUser
```commandline
py manage.py createsuperuser
```

_N.B: Currently Using sqlite database for development purpose._

**_N.B: Never work on master branch. Create your own branch to work on._**