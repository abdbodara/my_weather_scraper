# My Weather Scraper

## Run Code project

For creating new database

```For
sudo -i -u postgres
psql
CREATE USER postgres WITH PASSWORD 'postgres';
CREATE DATABASE guestbook OWNER postgres;
```

Setup other components

```
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate (For MACOS / Linux) OR venv\Scripts\activate (For Windows)

cd my_weather_scraper

pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

```

```
