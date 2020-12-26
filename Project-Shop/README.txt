EOIN STANKARD - G00300390
Data Representation Project

Server - "server.py"
SQL Code - "ProjectShop.py"
HTML File - "/staticpages/ProjectShop.html"
DB Config - "dbconfig.py"
MYSQL DB - "createDatabase.py"
MYSQL Tables - "createTable.py"
	- CREATE TABLE shop (id INT AUTO_INCREMENT PRIMARY KEY,product VARCHAR(255), price DOUBLE);
	- CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(255), quantity INT,price VARCHAR(255));


** HOW TO RUN **
LOCAL MACHINE:
    1. Make sure Git repo is fully downloaded "git clone https://github.com/EoinStankard/dataRepresentation.git"
    2. Create DB and tables (shop and customer) using above commands
	- Update "dbconfig.py" with your db username password and database name
    3. Open ProjectShop.html and make sure line 127 - "host = "http://127.0.0.1:5000"" is not commented out 
        - Line 126  //host = window.location.origin
        - Line 127    host = "http://127.0.0.1:5000"
    4. Run "python server.py"
    5. Open browser and got to "http://127.0.0.1:5000/ProjectShop.html"
    6. Create multiple shop products,update price and delete product
    7. Add to cart to put into customers shopping list

PYTHON ANYWHERE:
    1. http://eoinstankard.pythonanywhere.com/ProjectShop.html

    NOTE - I have noticed that sometimes the DB seems to disconnect, If this happens please do the following as it does work

    1. Clone repo to python anywhere and make sure ProjectShop.html is updated
	- Line 126    host = window.location.origin
        - Line 127    //host = "http://127.0.0.1:5000"
    2. Create Virtual machine in bash console - "mkvirtualenv --python=/usr/bin/python3.7 venv"
    3. Install requirements - "pip install -r requirements.txt"
    4. Create database and use commands for tables in MYSQL console
	- CREATE TABLE shop (id INT AUTO_INCREMENT PRIMARY KEY,product VARCHAR(255), price DOUBLE);
	- CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(255), quantity INT,price VARCHAR(255));
    5. Go back to bash console and update "dbconfig.py" with python anywhere db details
    