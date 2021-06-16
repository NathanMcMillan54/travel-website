# Travel Website

This is a Flask app for a project at school

Writing input to SQL doesn't work (properly), so this sorta uses a "nosql" database

#### Project structure
``db/`` - Data Base

&nbsp;&nbsp;&nbsp;&nbsp;``db/byte_db.txt`` - User input text database

&nbsp;&nbsp;&nbsp;&nbsp;``db/empty_main_db.sql`` - Should be the database

---

``static/`` - CSS/JS

&nbsp;&nbsp;&nbsp;&nbsp;``static/main.css`` - Main CSS file

---

``templates/`` - HTML

&nbsp;&nbsp;&nbsp;&nbsp;``templates/booking.html`` - Booking page (127.0.0.1:5000/booking)[127.0.0.1:500/booking]

&nbsp;&nbsp;&nbsp;&nbsp;``templates/index.html`` - Main page (127.0.0.1:5000/)[127.0.0.1:5000/]

#### Install

```commandline
sudo apt-get install sqlite3 # An SQL command for Linux
python3 -m venv venv && source venv/bin/activate # Create a virtual environement and activate it to install python requirements
pip install -r requirements.txt # Python requirements
```

#### Running (for Linux)

```commandline
python3 main.py
google-chrome 127.0.0.1:5000 # Or whatever you use
```
