# restAPI - DATA REPRESENTATION PROJECT

<img src='static_pages\images\restapi.png'>

<br>
<h2 style=color:#DDA0DD><b><u>Table of Contents</b></u></h2></summary>
  <ol>
    <li><a href='#Description'> Description</a></li>
    <li><a href='#Contents'>Repository Contents</a></li>
    <li><a href="#tables">Database Tables</a></li>
    <li><a href="#get">How To Get The Respoistory on Your Machine</a></li>
    <li><a href="#app">Running Application On Local Server</a></li>
    <li><a href="#host">Pythonanywhere Link</a></li>
    <li><a href="#ref">References</a></li> 
  </ol>

<br>
<h2><b><u><p id='Description'> Description</b></u></p></h2>

This repository contains all files, scripts and documentation for final the Data Representation module. The aim of this project is to to demonstrate that you understand creating and consuming RESTful APIs. My restAPI allows users to login/register and to display, create, update and delete their web bookmarks.


<h3>Objectives</h3>

- Create a Web application in Flask that has a REST API.
- The application should link to one or more database tables.
- Create accompanying web interface, using AJAX calls, to perform these CRUD operations


<br>

---

<h2><b><u><p id='Contents'>Repository Contents</b></u></p></h2>

- ```static_pages``` - Folder containing three web HTML pages (index.html, login.html, main.html), css folder and images folder.
- ````application.py```` - Flask server.
- ````createDB.py```` - Script to create the database and tables.
- ```bookmarksDAO.py``` - Creates a data access object (DAO) to interact with the created database.
- ```project_brief.pdf``` - The project brief.
- ```requirements.txt``` - The package requirements to run the project.


---

<h2><b><u><p id='tables'>Database Tables</b></u></p></h2>

 The ```datarep``` database consists of two tables:

<h3>1. users</h3>

<img src='static_pages\images\users_table.png'>

<br>

<h3>2. bookmarks</h3>

<img src='static_pages\images\bookmarks_table.png'>

<br>

```username``` in the ```bookmarks``` table is a foregin key.

 ---

<h2><b><u><p id='get'> How To Get The Repository on Your Machine</b></u></p></h2>
<br>
<ol>

<li>Using your browser navigate to the repository:  

https://github.com/kmcd14/restAPI


<br> </il>



<img src='static_pages\images\repository.png'>

<br>

<li>Under clone, copy the repository address, as seen in the above picture, using either SSH or HTTPS</li>
<li> Open your terminal.</li>
<li> Navigate to the location where you want to store the cloned directory.</li>
<li>In the terminal type the command:

<br>

<br>

    
    $git clone git@github.com:kmcd14/restAPI.git

<br>
</li>
<li>Press enter. The cloned repository is now on your machine.
</li>
<li> To install the necessary packages in the same directory type the command: 

<br>

    $pip install -r requirements.txt


Check the packages have been installed by typing the command: 

     $pip freeze
</ol>


---

<h2><b><u><p id='app'> Running Application On Local Server</b></u></p></h2>

1. Navigate to the the folder where you cloned the repository.

2. Create a new file called ```dbconfig.py``` and copy and paste the following:

```
   mysql = {
        'host': 'localhost',
         'user': 'username',
         'password': 'apassword',
         'database': 'datarep'
  }

```


replace the `username` and `apassword` values with your own details.

3. To create the database ```datarep``` and the two tables ```users``` and ```bookmarks```. Open teminal and type the command:

        $python createDatabase.py

4. Once the database and tables are created, type the following command into the terminal:

          $python application.py

5. Flask is now running. Open your browser and navigate to ```http://127.0.0.1:5000```.



---

<h2><b><u><p id='host'>PythonAnywhere Hosting</b></u></p></h2>

The application is hosted on ```pythonanywhere``` at: http://g00398279.pythonanywhere.com/index.html/


I have added some data to the database you can register your own user or login with:

- username: ```mulder```
- password: ```aliens```

 ---


<h2><b><u><p id='ref'>References</b></u></p></h2>

1.	Beatty A. Data Representation [Internet]. 2022. Available from: https://vlegalwaymayo.atu.ie/course/view.php?id=6209
 	 
2.	How do I specify unique constraint for multiple columns in MySQL? [Internet]. Stack Overflow. [cited 2022 Dec 18]. Available from: https://stackoverflow.com/questions/635937/how-do-i-specify-unique-constraint-for-multiple-columns-in-mysql
 	 
3.	Pixabay.com. [cited 2022 Dec 18]. Available from: https://pixabay.com/photos/books-bookstore-book-reading-1204029/
 	 
4.	Venkatesan N. Create and deploy a simple web application with flask and heroku [Internet]. Towards Data Science. 2021 [cited 2022 Dec 18]. Available from: https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb
 	 
5.	Python AttributeError: “str” object has no attribute “decode” [Internet]. Stack Overflow. [cited 2022 Dec 18]. Available from: https://stackoverflow.com/questions/50979667/python-attributeerror-str-object-has-no-attribute-decode
 	 
6.	How to read Windows environment variable value? [Internet]. Stack Overflow. [cited 2022 Dec 18]. Available from: https://stackoverflow.com/questions/10496748/how-to-read-windows-environment-variable-value
 	 
7.	Git. Bootstrap Navbar with logo centered above navbar [Internet]. Coding Yaar. 2020 [cited 2022 Dec 18]. Available from: https://codingyaar.com/responsive-bootstrap-navbar-with-logo-centered-above-navbar/
 	 
8.	Framework. How to fix Import could not be resolved from source Pylance [Internet]. Youtube; 2021 [cited 2022 Dec 18]. Available from: https://www.youtube.com/watch?v=5ud9Y2uB4PY
 	 
9.	Pixabay.com. [cited 2022 Dec 18]. Available from: https://cdn.pixabay.com/photo/2020/04/26/01/34/books-5093228_960_720.png
 	 
10.	How to create a filter/search table [Internet]. W3schools.com. [cited 2022 Dec 19]. Available from: https://www.w3schools.com/howto/howto_js_filter_table.asp

11. Jquery Ajax url path Issue [Internet]. Stack Overflow. [cited 2022 Dec 23]. Available from: https://stackoverflow.com/questions/24627075/jquery-ajax-url-path-issue

12. PythonAnywhere LLP. Forums [Internet]. Pythonanywhere.com. [cited 2022 Dec 24]. Available from: https://www.pythonanywhere.com/forums/topic/32182/


