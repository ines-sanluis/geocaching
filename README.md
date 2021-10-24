GEOCACHING
======

# SYSTEM REQUIREMENTS

Install pyenv https://github.com/pyenv/pyenv

```
sudo apt install python3-pip

if [ ! -d ".venv" ]
then
    pyenv install 3.7.6
    pyenv local 3.7.6
    pip install virtualenv
    virtualenv .venv
fi
```

# API
If DEV=1 all external requests will be mocked. Omitting it will use real external requests

```
. .venv/bin/activate
cd api
pip install -r requirements.txt
DEV=1 python3 app.py
```

# WEBAPP
```
cd webapp
npm install
npm run serve
```
