
<h1 align="center">
  <br>
  <a href="https://github.com/emayolle/django_final"><img src="https://raw.githubusercontent.com/emayolle/django_final/main/git_images/logo.png" alt="Movie Searcher" width="200"></a>
  <br>
  Movie Searcher
  <br>
</h1>

<h4 align="center">A web application made with <code>django</code> that allows a user to search a movie by title and display the result(s).</h4>


<p align="center">
  <a href="#context">Context</a> •
  <a href="#todo-list">Todo List</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/emayolle/django_final/main/git_images/exemple.gif)

## Context
This project is part of my third year of study at [Junia](https://junia.com/) in the [Computer Science](https://www.junia.com/fr/fiches-metiers/ingenieur-developpeur/) program. I am currently in an apprenticeship at [Roquette LESTREM](https://fr.roquette.com/) as a DevOps Engineer. To validate my Python module, I was asked to create a web application with Django. The subject of this evaluation is to deliver a Python / Django application that meets the following specifications. The purpose of the application is to allow a user to search for a movie in a database and display the result(s). If no result is known, the application will then search for the results in a third-party API. The expected behaviors are as follows:
- At the launch of the application, a form is presented to the user, the user can enter a movie title (example: star wars) in a search bar and validate the form.
- The application must respond with the corresponding results found in the database.
- If no result is found in the database, the application will then search for the results in the API and display them to the user. These results are saved in the database to be reused if necessary.

> **Note**
> The full specifications file can be found in the root of the project under the name [Django_Final.pdf](https://github.com/emayolle/django_final/blob/main/Django_Final.pdf).
## Key Features

* Searching a movie by title
  - The user can search for a movie by title in the database.
  - If no result is known, the application will then search for the results in a third-party API.
  > **Note**
  > The third-party API used is [OMDb API](http://www.omdbapi.com/).
* Cross platform
  - Windows, macOS and Linux ready.


## Todo List

- [x] Index page with a search bar
- [x] Search for a movie in the database
- [x] Display the results to the user
- [x] Search for a movie in the [OMDb API](http://www.omdbapi.com/)
- [x] Save the results in the database if they are found in the API
- [x] Documentation of the project
- [ ] Unit tests

## Installation
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. Once you have Python installed, you can clone the project using the following command:
```bash
git clone git@github.com:emayolle/django_final.git
```
Then, you need to install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

## How To Use
To use the project, you need to run the following command:
```bash
python manage.py makemigrations movie_searcher
python manage.py migrate
python manage.py runserver
```
Then, you can access the application by going to the following URL: [http://localhost:8000/](http://localhost:8000/)

<!-- 
> **Note**
> If you're using Linux Bash you can do `python manage.py shell < generate_data.py` to generate some data in the database.
-->

## Credits

- Application created by [Erwan Mayolle](https://github.com/emayolle).
- This readme is using the template created by [amitmerchant1990](https://github.com/amitmerchant1990).

## License

MIT

---

> GitHub [@emayolle](https://github.com/emayolle)

