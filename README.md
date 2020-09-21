# Tutorial-Django

Belajar Django Framework, sumber referensi tutorial dari channel Youtube Kelas Terbua [Django Kelas Terbuka](https://www.youtube.com/watch?v=hPXNP1NoVNQ&list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld&index=1)

## `Setup Windows`

1. Download and Install python. Go to [https://www.python.org/](https://www.python.org/).
2. Check python in your computer `$ python --version`.
3. Check pip `$ pip list`. If pip need to upgrade please upgrade first.
4. Create a Virtual Environment `$ python -m venv Env`
5. Activate the Env, type in the terminal `$ D:\Wilden github\Tutorial-Django>Env\Scripts\activate.bat`
6. Check pip list in the (Env). Upgrade if need it `$ python.exe -m pip install --upgrade pip`. Check again
7. Install Django Versi `1.11.*` `$ pip install Django==1.11.*`. Star mean will get the last version off 1.11. django.
8. `$ pip list` to check django already installed or not.
9. Create project `$ django-admin startproject mywebsite`.
10. How to run django server.

- Go to mywebsite directory `$ cd mywebsite`
- Type `$ manage.py runserver` to run the django server
- Open [http://localhost:8000/](http://localhost:8000/) in web browser

## `Pengenalan Project`

1. Type some script in urls.py
2. Test in web browser

- [http://localhost:8000](http://localhost:8000)
- [http://localhost:8000/about](http://localhost:8000/about)

## `Pengenalan Views`

1. Create a file named views.py inside mywebsite directory
2. Cut script from urls.py and paste to views.py then edit little bit

## `Pengenalan Templates`

1. Go to settings.py and find TEMPLATES =[] (line 54)
2. Change `'DIRS': [],` to be `'DIRS': ['templates'],`
3. Create a directory named `templates`
4. Create a file named `index.html` inside templates directory

## `Pengenalan App`

1. Create a new App

- Stop server
- Create an App `$ python manage.py startapp blog`
- Run server `$ python manage.py runserver`

2. Give some script in `veiws.py` file in blog directory
3. Create a file named `blog.html`
4. Edit script in urls.py file
5. Test with open the url [http://localhost:8000/blog/](http://localhost:8000/blog/) in web browser
