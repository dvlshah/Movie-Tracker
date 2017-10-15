Web application for tracking movies

This project is done on python3 with DJANGO backend.
Make sure you have install python3 in your machine.

| ------------------------|
| How to run the project? |
| ------------------------|

    [1]Clone the project in your local machine.
    [2]First create a virtual env --> http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv
    [3]After starting virtual environment go to the movietracker dir.
    [4]Install all the dependencies by pip3 install -r requirements.txt.
    [5]Check all the dependencies is fulfilled using pip3 freeze
    [6]Go to movietracker/,open the terminal and run command python3 manage.py runserver
    [7]Go to the urls mentioned below.

|------|
| URLS |
|------|

[1]http://127.0.0.1:8000/admin/movies/
  --> This url goes to admin GUI for doing CRUD operations on
      Movies table(adding movies,deleting,updating etc.)
[2]http://127.0.0.1:8000/admin/actor/
  --> This url goes to admin GUI for doing CRUD operations on
      Actor table(adding actors,deleting,updating etc.)
[3]http://127.0.0.1:8000/admin/director/
  --> This url goes to admin GUI for doing CRUD operations on
      Director table(adding director,deleting,updating etc.)
[4]http://127.0.0.1:8000/movies/movies/
  --> This url goes to HTML page for displaying movies with
      paginator included (10 movies per page).
[5]http://127.0.0.1:8000/api/movies/
  --> This url goes to HTML page for displaying data of movies in
      json format through REST API of Movies table in database.
[6]http://127.0.0.1:8000/api/movies/edit
  --> This url goes to HTML page for displaying and editing
      json formatted data through REST API of Movies
[7]http://127.0.0.1:8000/api/movies/delete
--> This url goes to HTML page for displaying and deleting
    json formatted data through REST API of Movies
