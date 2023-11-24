# zomatochronicles
## .env ( Postgres Only )
 ```bash
DATABASE_ENGINE=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=

   ```
# Installation
## windows
 ```bash
git clone https://github.com/bethimanideep/zomatochronicles.git
cd zomatochronicles
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python app.py
   ```
## linux
 ```bash
git clone 
cd zomatochronicles
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 app.py
   ```
