README
This will be split into 3 sections, downloads, installs, and running of the files.

DOWNLOADS

python 3.7.1
MySQL workbench, shell, server, python connector
XAMPP
Python IDE or compiler

MODULES FOR PYTHON
PyGame
MySQL python connector 8.0
Pickle
Sockets


Follow the installer for Python, pycharm, MySQL workbench, XAMPP,
Installing PHP
In your XAMPP folder, locate the HTdocs folder. Paste in all of the code in the php file, 
which should include 5 files, 4 php files and one css file.


INSTALLATION
Install python
Follow through the python installer guide, and make a note of where it is saved.
Install pycharm or another IDE
Install pycharm using its installation wizard, and make a new project named BubblePoppers.
Inside that file, BubblePoppers, you should see a default folder created called venv. Inside venv is a folder called Scripts,
and go inside Scripts. 
Once inside scripts, you are going to need to command line to that location and start installing the modules needed.
So once you have your command line cd'd inside of Scripts, type

pip install pygame

and wait for it to install. Then type 

pip install sockets

and wait for it to install. Then type

pip install network

and wait for it to install. Then type 

pip install pickle

and wait for it to install. Then type 

pip install threading

and wait for it to install. 
These are the main downloads needed for the server and client to run, and in such are mandatory to run the game. 
All of them should have been installed in your Scripts folder in your venv in your project folder.

If you decide to run the website and database to track wins, you should also type

pip install mysql.connector

Make sure your XAMPP and SQL were installed correctly, and running on the same port number.



RUNNING THE PROJECT
You should start your XAMPP mySQL and apache servers, and then connect to the server on port 80 through MySQL workbench.
Run the database script, and check the website by typing 'localhost' into your browser. You should see the home page 
for BubblePoppers.
Make an account on the account page, and check that it was created by checking the leaderboard page. 
Make a note of your ID, as that number should be set in one of the python files.
Go into client, and on line 65 and 74, change UserID = 'x', x being your ID.
After this has been set up, you should be able to run the python file server.py. 
Only one person needs to run this file, and both users should update their network.py files to reflect the same IP address
as the server IP address.
Run the python server, and have both users run the python client.

***Make sure you have the wifi you are trying it on set as a private***
***or home network so you dont have any firewall issues.***
