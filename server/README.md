# SocialWiki Server

## Requirements
- python 3
- pip

## Installation
### Commands
```
cd server
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

### If bugs
```
pip install flask-cors flask-restful
```

## Run the server
```
python server.py
```
