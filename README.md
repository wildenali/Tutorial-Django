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
3. Create a file named `blog.html` in templates directory
4. Edit script in urls.py file
5. Test with open the url [http://localhost:8000/blog/](http://localhost:8000/blog/) in web browser

6. Create a new App named About

- Stop server
- Create an App `$ python manage.py startapp about`
- Run server `$ python manage.py runserver`

7. Give some script in `veiws.py` file in blog directory
8. Create a file named `about.html` in templates directory
9. Edit script in urls.py file
10. Test with open the url [http://localhost:8000/about/](http://localhost:8000/about/) in web browser

## `Menggunakan URL pada App`

1. Create a `urls.py` file inside blog directory
2. Create a new def named `def recent:` on views.py inside blog directory

- How to test is open [http://localhost:8000/blog/recent/](http://localhost:8000/blog/recent/)

## `Template pada App`

1. Go to mywebsite directory and open setting.py file
2. Add app blog inside INSTALLED_APPS, see following below

```
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'blog',
]
```

3. Go to blog directory > Create a new directory named `templates` and Create a new directory `blog` inside templates directory
4. Go to mywebsite > templates, and Cut `blog.html`
5. Go to mywebsite > blog > templates > blog, and paste `blog.html` file

- Test, Open [http://localhost:8000/blog/](http://localhost:8000/blog/)
- Change the name `blog.html` to be `index.html`
- Test again, Open [http://localhost:8000/blog/](http://localhost:8000/blog/)

## `Template Variable`

1. Passing the variable from views.py to index.html
2. Edit mywebsite\views.py and tamplates\index.html
3. Test with [http://localhost:8000/](http://localhost:8000/)
4. Passing the variable from blog\views.py to mywebsite\index.html
5. Edit blog\views.py
6. Test with [http://localhost:8000/blog/](http://localhost:8000/blog/)
7. Passing the variable from blog\views.py to blog\templates\blog\index.html
8. Edit blog\views.py
9. Test with [http://localhost:8000/blog/cerita/](http://localhost:8000/blog/cerita/)
10. Passing the variable news from blog\views.py to blog\templates\blog\index.html
11. Edit blog\views.py
12. Test with [http://localhost:8000/blog/news/](http://localhost:8000/blog/news/)
